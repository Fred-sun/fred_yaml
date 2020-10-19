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
module: azure_rm_streamingpolicy_info
version_added: '2.9'
short_description: Get StreamingPolicy info.
description:
  - Get info of StreamingPolicy.
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
  streaming_policy_name:
    description:
      - The Streaming Policy name.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Lists Streaming Policies
      azure_rm_streamingpolicy_info: 
        account_name: contosomedia
        resource_group_name: contoso
        

    - name: Get a Streaming Policy by name
      azure_rm_streamingpolicy_info: 
        account_name: contosomedia
        resource_group_name: contoso
        streaming_policy_name: clearStreamingPolicy
        

'''

RETURN = '''
streaming_policies:
  description: >-
    A list of dict results where the key is the name of the StreamingPolicy and
    the values are the facts for that StreamingPolicy.
  returned: always
  type: complex
  contains:
    value:
      description:
        - A collection of StreamingPolicy items.
      returned: always
      type: list
      sample: null
      contains:
        created:
          description:
            - Creation time of Streaming Policy
          returned: always
          type: str
          sample: null
        default_content_key_policy_name:
          description:
            - Default ContentKey used by current Streaming Policy
          returned: always
          type: str
          sample: null
        envelope_encryption:
          description:
            - Configuration of EnvelopeEncryption
          returned: always
          type: dict
          sample: null
          contains:
            enabled_protocols:
              description:
                - Representing supported protocols
              returned: always
              type: dict
              sample: null
              contains:
                download:
                  description:
                    - Enable Download protocol or not
                  returned: always
                  type: bool
                  sample: null
                dash:
                  description:
                    - Enable DASH protocol or not
                  returned: always
                  type: bool
                  sample: null
                hls:
                  description:
                    - Enable HLS protocol or not
                  returned: always
                  type: bool
                  sample: null
                smooth_streaming:
                  description:
                    - Enable SmoothStreaming protocol or not
                  returned: always
                  type: bool
                  sample: null
            clear_tracks:
              description:
                - Representing which tracks should not be encrypted
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
            content_keys:
              description:
                - >-
                  Representing default content key for each encryption scheme
                  and separate content keys for specific tracks
              returned: always
              type: dict
              sample: null
              contains:
                default_key:
                  description:
                    - Default content key for an encryption scheme
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    label:
                      description:
                        - >-
                          Label can be used to specify Content Key when creating
                          a Streaming Locator
                      returned: always
                      type: str
                      sample: null
                    policy_name:
                      description:
                        - Policy used by Default Key
                      returned: always
                      type: str
                      sample: null
                key_to_track_mappings:
                  description:
                    - Representing tracks needs separate content key
                  returned: always
                  type: list
                  sample: null
                  contains:
                    label:
                      description:
                        - >-
                          Label can be used to specify Content Key when creating
                          a Streaming Locator
                      returned: always
                      type: str
                      sample: null
                    policy_name:
                      description:
                        - Policy used by Content Key
                      returned: always
                      type: str
                      sample: null
                    tracks:
                      description:
                        - Tracks which use this content key
                      returned: always
                      type: list
                      sample: null
                      contains:
                        track_selections:
                          description:
                            - >-
                              TrackSelections is a track property condition list
                              which can specify track(s)
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
            custom_key_acquisition_url_template:
              description:
                - >-
                  Template for the URL of the custom service delivering keys to
                  end user players.  Not required when using Azure Media
                  Services for issuing keys.  The template supports replaceable
                  tokens that the service will update at runtime with the value
                  specific to the request.  The currently supported token values
                  are {AlternativeMediaId}, which is replaced with the value of
                  StreamingLocatorId.AlternativeMediaId, and {ContentKeyId},
                  which is replaced with the value of identifier of the key
                  being requested.
              returned: always
              type: str
              sample: null
        common_encryption_cenc:
          description:
            - Configuration of CommonEncryptionCenc
          returned: always
          type: dict
          sample: null
          contains:
            enabled_protocols:
              description:
                - Representing supported protocols
              returned: always
              type: dict
              sample: null
              contains:
                download:
                  description:
                    - Enable Download protocol or not
                  returned: always
                  type: bool
                  sample: null
                dash:
                  description:
                    - Enable DASH protocol or not
                  returned: always
                  type: bool
                  sample: null
                hls:
                  description:
                    - Enable HLS protocol or not
                  returned: always
                  type: bool
                  sample: null
                smooth_streaming:
                  description:
                    - Enable SmoothStreaming protocol or not
                  returned: always
                  type: bool
                  sample: null
            clear_tracks:
              description:
                - Representing which tracks should not be encrypted
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
            content_keys:
              description:
                - >-
                  Representing default content key for each encryption scheme
                  and separate content keys for specific tracks
              returned: always
              type: dict
              sample: null
              contains:
                default_key:
                  description:
                    - Default content key for an encryption scheme
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    label:
                      description:
                        - >-
                          Label can be used to specify Content Key when creating
                          a Streaming Locator
                      returned: always
                      type: str
                      sample: null
                    policy_name:
                      description:
                        - Policy used by Default Key
                      returned: always
                      type: str
                      sample: null
                key_to_track_mappings:
                  description:
                    - Representing tracks needs separate content key
                  returned: always
                  type: list
                  sample: null
                  contains:
                    label:
                      description:
                        - >-
                          Label can be used to specify Content Key when creating
                          a Streaming Locator
                      returned: always
                      type: str
                      sample: null
                    policy_name:
                      description:
                        - Policy used by Content Key
                      returned: always
                      type: str
                      sample: null
                    tracks:
                      description:
                        - Tracks which use this content key
                      returned: always
                      type: list
                      sample: null
                      contains:
                        track_selections:
                          description:
                            - >-
                              TrackSelections is a track property condition list
                              which can specify track(s)
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
            drm:
              description:
                - >-
                  Configuration of DRMs for CommonEncryptionCenc encryption
                  scheme
              returned: always
              type: dict
              sample: null
              contains:
                play_ready:
                  description:
                    - PlayReady configurations
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    custom_license_acquisition_url_template:
                      description:
                        - >-
                          Template for the URL of the custom service delivering
                          licenses to end user players.  Not required when using
                          Azure Media Services for issuing licenses.  The
                          template supports replaceable tokens that the service
                          will update at runtime with the value specific to the
                          request.  The currently supported token values are
                          {AlternativeMediaId}, which is replaced with the value
                          of StreamingLocatorId.AlternativeMediaId, and
                          {ContentKeyId}, which is replaced with the value of
                          identifier of the key being requested.
                      returned: always
                      type: str
                      sample: null
                    play_ready_custom_attributes:
                      description:
                        - Custom attributes for PlayReady
                      returned: always
                      type: str
                      sample: null
                widevine:
                  description:
                    - Widevine configurations
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    custom_license_acquisition_url_template:
                      description:
                        - >-
                          Template for the URL of the custom service delivering
                          licenses to end user players.  Not required when using
                          Azure Media Services for issuing licenses.  The
                          template supports replaceable tokens that the service
                          will update at runtime with the value specific to the
                          request.  The currently supported token values are
                          {AlternativeMediaId}, which is replaced with the value
                          of StreamingLocatorId.AlternativeMediaId, and
                          {ContentKeyId}, which is replaced with the value of
                          identifier of the key being requested.
                      returned: always
                      type: str
                      sample: null
        common_encryption_cbcs:
          description:
            - Configuration of CommonEncryptionCbcs
          returned: always
          type: dict
          sample: null
          contains:
            enabled_protocols:
              description:
                - Representing supported protocols
              returned: always
              type: dict
              sample: null
              contains:
                download:
                  description:
                    - Enable Download protocol or not
                  returned: always
                  type: bool
                  sample: null
                dash:
                  description:
                    - Enable DASH protocol or not
                  returned: always
                  type: bool
                  sample: null
                hls:
                  description:
                    - Enable HLS protocol or not
                  returned: always
                  type: bool
                  sample: null
                smooth_streaming:
                  description:
                    - Enable SmoothStreaming protocol or not
                  returned: always
                  type: bool
                  sample: null
            clear_tracks:
              description:
                - Representing which tracks should not be encrypted
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
            content_keys:
              description:
                - >-
                  Representing default content key for each encryption scheme
                  and separate content keys for specific tracks
              returned: always
              type: dict
              sample: null
              contains:
                default_key:
                  description:
                    - Default content key for an encryption scheme
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    label:
                      description:
                        - >-
                          Label can be used to specify Content Key when creating
                          a Streaming Locator
                      returned: always
                      type: str
                      sample: null
                    policy_name:
                      description:
                        - Policy used by Default Key
                      returned: always
                      type: str
                      sample: null
                key_to_track_mappings:
                  description:
                    - Representing tracks needs separate content key
                  returned: always
                  type: list
                  sample: null
                  contains:
                    label:
                      description:
                        - >-
                          Label can be used to specify Content Key when creating
                          a Streaming Locator
                      returned: always
                      type: str
                      sample: null
                    policy_name:
                      description:
                        - Policy used by Content Key
                      returned: always
                      type: str
                      sample: null
                    tracks:
                      description:
                        - Tracks which use this content key
                      returned: always
                      type: list
                      sample: null
                      contains:
                        track_selections:
                          description:
                            - >-
                              TrackSelections is a track property condition list
                              which can specify track(s)
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
            drm:
              description:
                - Configuration of DRMs for current encryption scheme
              returned: always
              type: dict
              sample: null
              contains:
                fair_play:
                  description:
                    - FairPlay configurations
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    custom_license_acquisition_url_template:
                      description:
                        - >-
                          Template for the URL of the custom service delivering
                          licenses to end user players.  Not required when using
                          Azure Media Services for issuing licenses.  The
                          template supports replaceable tokens that the service
                          will update at runtime with the value specific to the
                          request.  The currently supported token values are
                          {AlternativeMediaId}, which is replaced with the value
                          of StreamingLocatorId.AlternativeMediaId, and
                          {ContentKeyId}, which is replaced with the value of
                          identifier of the key being requested.
                      returned: always
                      type: str
                      sample: null
                    allow_persistent_license:
                      description:
                        - All license to be persistent or not
                      returned: always
                      type: bool
                      sample: null
                play_ready:
                  description:
                    - PlayReady configurations
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    custom_license_acquisition_url_template:
                      description:
                        - >-
                          Template for the URL of the custom service delivering
                          licenses to end user players.  Not required when using
                          Azure Media Services for issuing licenses.  The
                          template supports replaceable tokens that the service
                          will update at runtime with the value specific to the
                          request.  The currently supported token values are
                          {AlternativeMediaId}, which is replaced with the value
                          of StreamingLocatorId.AlternativeMediaId, and
                          {ContentKeyId}, which is replaced with the value of
                          identifier of the key being requested.
                      returned: always
                      type: str
                      sample: null
                    play_ready_custom_attributes:
                      description:
                        - Custom attributes for PlayReady
                      returned: always
                      type: str
                      sample: null
                widevine:
                  description:
                    - Widevine configurations
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    custom_license_acquisition_url_template:
                      description:
                        - >-
                          Template for the URL of the custom service delivering
                          licenses to end user players.  Not required when using
                          Azure Media Services for issuing licenses.  The
                          template supports replaceable tokens that the service
                          will update at runtime with the value specific to the
                          request.  The currently supported token values are
                          {AlternativeMediaId}, which is replaced with the value
                          of StreamingLocatorId.AlternativeMediaId, and
                          {ContentKeyId}, which is replaced with the value of
                          identifier of the key being requested.
                      returned: always
                      type: str
                      sample: null
        no_encryption:
          description:
            - Configurations of NoEncryption
          returned: always
          type: dict
          sample: null
          contains:
            enabled_protocols:
              description:
                - Representing supported protocols
              returned: always
              type: dict
              sample: null
              contains:
                download:
                  description:
                    - Enable Download protocol or not
                  returned: always
                  type: bool
                  sample: null
                dash:
                  description:
                    - Enable DASH protocol or not
                  returned: always
                  type: bool
                  sample: null
                hls:
                  description:
                    - Enable HLS protocol or not
                  returned: always
                  type: bool
                  sample: null
                smooth_streaming:
                  description:
                    - Enable SmoothStreaming protocol or not
                  returned: always
                  type: bool
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
    created:
      description:
        - Creation time of Streaming Policy
      returned: always
      type: str
      sample: null
    default_content_key_policy_name:
      description:
        - Default ContentKey used by current Streaming Policy
      returned: always
      type: str
      sample: null
    envelope_encryption:
      description:
        - Configuration of EnvelopeEncryption
      returned: always
      type: dict
      sample: null
      contains:
        enabled_protocols:
          description:
            - Representing supported protocols
          returned: always
          type: dict
          sample: null
          contains:
            download:
              description:
                - Enable Download protocol or not
              returned: always
              type: bool
              sample: null
            dash:
              description:
                - Enable DASH protocol or not
              returned: always
              type: bool
              sample: null
            hls:
              description:
                - Enable HLS protocol or not
              returned: always
              type: bool
              sample: null
            smooth_streaming:
              description:
                - Enable SmoothStreaming protocol or not
              returned: always
              type: bool
              sample: null
        clear_tracks:
          description:
            - Representing which tracks should not be encrypted
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
        content_keys:
          description:
            - >-
              Representing default content key for each encryption scheme and
              separate content keys for specific tracks
          returned: always
          type: dict
          sample: null
          contains:
            default_key:
              description:
                - Default content key for an encryption scheme
              returned: always
              type: dict
              sample: null
              contains:
                label:
                  description:
                    - >-
                      Label can be used to specify Content Key when creating a
                      Streaming Locator
                  returned: always
                  type: str
                  sample: null
                policy_name:
                  description:
                    - Policy used by Default Key
                  returned: always
                  type: str
                  sample: null
            key_to_track_mappings:
              description:
                - Representing tracks needs separate content key
              returned: always
              type: list
              sample: null
              contains:
                label:
                  description:
                    - >-
                      Label can be used to specify Content Key when creating a
                      Streaming Locator
                  returned: always
                  type: str
                  sample: null
                policy_name:
                  description:
                    - Policy used by Content Key
                  returned: always
                  type: str
                  sample: null
                tracks:
                  description:
                    - Tracks which use this content key
                  returned: always
                  type: list
                  sample: null
                  contains:
                    track_selections:
                      description:
                        - >-
                          TrackSelections is a track property condition list
                          which can specify track(s)
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
        custom_key_acquisition_url_template:
          description:
            - >-
              Template for the URL of the custom service delivering keys to end
              user players.  Not required when using Azure Media Services for
              issuing keys.  The template supports replaceable tokens that the
              service will update at runtime with the value specific to the
              request.  The currently supported token values are
              {AlternativeMediaId}, which is replaced with the value of
              StreamingLocatorId.AlternativeMediaId, and {ContentKeyId}, which
              is replaced with the value of identifier of the key being
              requested.
          returned: always
          type: str
          sample: null
    common_encryption_cenc:
      description:
        - Configuration of CommonEncryptionCenc
      returned: always
      type: dict
      sample: null
      contains:
        enabled_protocols:
          description:
            - Representing supported protocols
          returned: always
          type: dict
          sample: null
          contains:
            download:
              description:
                - Enable Download protocol or not
              returned: always
              type: bool
              sample: null
            dash:
              description:
                - Enable DASH protocol or not
              returned: always
              type: bool
              sample: null
            hls:
              description:
                - Enable HLS protocol or not
              returned: always
              type: bool
              sample: null
            smooth_streaming:
              description:
                - Enable SmoothStreaming protocol or not
              returned: always
              type: bool
              sample: null
        clear_tracks:
          description:
            - Representing which tracks should not be encrypted
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
        content_keys:
          description:
            - >-
              Representing default content key for each encryption scheme and
              separate content keys for specific tracks
          returned: always
          type: dict
          sample: null
          contains:
            default_key:
              description:
                - Default content key for an encryption scheme
              returned: always
              type: dict
              sample: null
              contains:
                label:
                  description:
                    - >-
                      Label can be used to specify Content Key when creating a
                      Streaming Locator
                  returned: always
                  type: str
                  sample: null
                policy_name:
                  description:
                    - Policy used by Default Key
                  returned: always
                  type: str
                  sample: null
            key_to_track_mappings:
              description:
                - Representing tracks needs separate content key
              returned: always
              type: list
              sample: null
              contains:
                label:
                  description:
                    - >-
                      Label can be used to specify Content Key when creating a
                      Streaming Locator
                  returned: always
                  type: str
                  sample: null
                policy_name:
                  description:
                    - Policy used by Content Key
                  returned: always
                  type: str
                  sample: null
                tracks:
                  description:
                    - Tracks which use this content key
                  returned: always
                  type: list
                  sample: null
                  contains:
                    track_selections:
                      description:
                        - >-
                          TrackSelections is a track property condition list
                          which can specify track(s)
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
        drm:
          description:
            - Configuration of DRMs for CommonEncryptionCenc encryption scheme
          returned: always
          type: dict
          sample: null
          contains:
            play_ready:
              description:
                - PlayReady configurations
              returned: always
              type: dict
              sample: null
              contains:
                custom_license_acquisition_url_template:
                  description:
                    - >-
                      Template for the URL of the custom service delivering
                      licenses to end user players.  Not required when using
                      Azure Media Services for issuing licenses.  The template
                      supports replaceable tokens that the service will update
                      at runtime with the value specific to the request.  The
                      currently supported token values are {AlternativeMediaId},
                      which is replaced with the value of
                      StreamingLocatorId.AlternativeMediaId, and {ContentKeyId},
                      which is replaced with the value of identifier of the key
                      being requested.
                  returned: always
                  type: str
                  sample: null
                play_ready_custom_attributes:
                  description:
                    - Custom attributes for PlayReady
                  returned: always
                  type: str
                  sample: null
            widevine:
              description:
                - Widevine configurations
              returned: always
              type: dict
              sample: null
              contains:
                custom_license_acquisition_url_template:
                  description:
                    - >-
                      Template for the URL of the custom service delivering
                      licenses to end user players.  Not required when using
                      Azure Media Services for issuing licenses.  The template
                      supports replaceable tokens that the service will update
                      at runtime with the value specific to the request.  The
                      currently supported token values are {AlternativeMediaId},
                      which is replaced with the value of
                      StreamingLocatorId.AlternativeMediaId, and {ContentKeyId},
                      which is replaced with the value of identifier of the key
                      being requested.
                  returned: always
                  type: str
                  sample: null
    common_encryption_cbcs:
      description:
        - Configuration of CommonEncryptionCbcs
      returned: always
      type: dict
      sample: null
      contains:
        enabled_protocols:
          description:
            - Representing supported protocols
          returned: always
          type: dict
          sample: null
          contains:
            download:
              description:
                - Enable Download protocol or not
              returned: always
              type: bool
              sample: null
            dash:
              description:
                - Enable DASH protocol or not
              returned: always
              type: bool
              sample: null
            hls:
              description:
                - Enable HLS protocol or not
              returned: always
              type: bool
              sample: null
            smooth_streaming:
              description:
                - Enable SmoothStreaming protocol or not
              returned: always
              type: bool
              sample: null
        clear_tracks:
          description:
            - Representing which tracks should not be encrypted
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
        content_keys:
          description:
            - >-
              Representing default content key for each encryption scheme and
              separate content keys for specific tracks
          returned: always
          type: dict
          sample: null
          contains:
            default_key:
              description:
                - Default content key for an encryption scheme
              returned: always
              type: dict
              sample: null
              contains:
                label:
                  description:
                    - >-
                      Label can be used to specify Content Key when creating a
                      Streaming Locator
                  returned: always
                  type: str
                  sample: null
                policy_name:
                  description:
                    - Policy used by Default Key
                  returned: always
                  type: str
                  sample: null
            key_to_track_mappings:
              description:
                - Representing tracks needs separate content key
              returned: always
              type: list
              sample: null
              contains:
                label:
                  description:
                    - >-
                      Label can be used to specify Content Key when creating a
                      Streaming Locator
                  returned: always
                  type: str
                  sample: null
                policy_name:
                  description:
                    - Policy used by Content Key
                  returned: always
                  type: str
                  sample: null
                tracks:
                  description:
                    - Tracks which use this content key
                  returned: always
                  type: list
                  sample: null
                  contains:
                    track_selections:
                      description:
                        - >-
                          TrackSelections is a track property condition list
                          which can specify track(s)
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
        drm:
          description:
            - Configuration of DRMs for current encryption scheme
          returned: always
          type: dict
          sample: null
          contains:
            fair_play:
              description:
                - FairPlay configurations
              returned: always
              type: dict
              sample: null
              contains:
                custom_license_acquisition_url_template:
                  description:
                    - >-
                      Template for the URL of the custom service delivering
                      licenses to end user players.  Not required when using
                      Azure Media Services for issuing licenses.  The template
                      supports replaceable tokens that the service will update
                      at runtime with the value specific to the request.  The
                      currently supported token values are {AlternativeMediaId},
                      which is replaced with the value of
                      StreamingLocatorId.AlternativeMediaId, and {ContentKeyId},
                      which is replaced with the value of identifier of the key
                      being requested.
                  returned: always
                  type: str
                  sample: null
                allow_persistent_license:
                  description:
                    - All license to be persistent or not
                  returned: always
                  type: bool
                  sample: null
            play_ready:
              description:
                - PlayReady configurations
              returned: always
              type: dict
              sample: null
              contains:
                custom_license_acquisition_url_template:
                  description:
                    - >-
                      Template for the URL of the custom service delivering
                      licenses to end user players.  Not required when using
                      Azure Media Services for issuing licenses.  The template
                      supports replaceable tokens that the service will update
                      at runtime with the value specific to the request.  The
                      currently supported token values are {AlternativeMediaId},
                      which is replaced with the value of
                      StreamingLocatorId.AlternativeMediaId, and {ContentKeyId},
                      which is replaced with the value of identifier of the key
                      being requested.
                  returned: always
                  type: str
                  sample: null
                play_ready_custom_attributes:
                  description:
                    - Custom attributes for PlayReady
                  returned: always
                  type: str
                  sample: null
            widevine:
              description:
                - Widevine configurations
              returned: always
              type: dict
              sample: null
              contains:
                custom_license_acquisition_url_template:
                  description:
                    - >-
                      Template for the URL of the custom service delivering
                      licenses to end user players.  Not required when using
                      Azure Media Services for issuing licenses.  The template
                      supports replaceable tokens that the service will update
                      at runtime with the value specific to the request.  The
                      currently supported token values are {AlternativeMediaId},
                      which is replaced with the value of
                      StreamingLocatorId.AlternativeMediaId, and {ContentKeyId},
                      which is replaced with the value of identifier of the key
                      being requested.
                  returned: always
                  type: str
                  sample: null
    no_encryption:
      description:
        - Configurations of NoEncryption
      returned: always
      type: dict
      sample: null
      contains:
        enabled_protocols:
          description:
            - Representing supported protocols
          returned: always
          type: dict
          sample: null
          contains:
            download:
              description:
                - Enable Download protocol or not
              returned: always
              type: bool
              sample: null
            dash:
              description:
                - Enable DASH protocol or not
              returned: always
              type: bool
              sample: null
            hls:
              description:
                - Enable HLS protocol or not
              returned: always
              type: bool
              sample: null
            smooth_streaming:
              description:
                - Enable SmoothStreaming protocol or not
              returned: always
              type: bool
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


class AzureRMStreamingPolicyInfo(AzureRMModuleBase):
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
            streaming_policy_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.filter = None
        self.top = None
        self.orderby = None
        self.streaming_policy_name = None

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
        super(AzureRMStreamingPolicyInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Azure Media Services,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-05-01')

        if (self.resource_group_name is not None and
            self.account_name is not None and
            self.streaming_policy_name is not None):
            self.results['streaming_policies'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.account_name is not None):
            self.results['streaming_policies'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.streaming_policies.get(resource_group_name=self.resource_group_name,
                                                               account_name=self.account_name,
                                                               streaming_policy_name=self.streaming_policy_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.streaming_policies.list(resource_group_name=self.resource_group_name,
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
    AzureRMStreamingPolicyInfo()


if __name__ == '__main__':
    main()
