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
module: azure_rm_streamingpolicy
version_added: '2.9'
short_description: Manage Azure StreamingPolicy instance.
description:
  - 'Create, update and delete instance of Azure StreamingPolicy.'
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
  streaming_policy_name:
    description:
      - The Streaming Policy name.
    required: true
    type: str
  default_content_key_policy_name:
    description:
      - Default ContentKey used by current Streaming Policy
    type: str
  envelope_encryption:
    description:
      - Configuration of EnvelopeEncryption
    type: dict
    suboptions:
      enabled_protocols:
        description:
          - Representing supported protocols
        type: dict
        suboptions:
          download:
            description:
              - Enable Download protocol or not
            required: true
            type: bool
          dash:
            description:
              - Enable DASH protocol or not
            required: true
            type: bool
          hls:
            description:
              - Enable HLS protocol or not
            required: true
            type: bool
          smooth_streaming:
            description:
              - Enable SmoothStreaming protocol or not
            required: true
            type: bool
      clear_tracks:
        description:
          - Representing which tracks should not be encrypted
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
      content_keys:
        description:
          - >-
            Representing default content key for each encryption scheme and
            separate content keys for specific tracks
        type: dict
        suboptions:
          default_key:
            description:
              - Default content key for an encryption scheme
            type: dict
            suboptions:
              label:
                description:
                  - >-
                    Label can be used to specify Content Key when creating a
                    Streaming Locator
                type: str
              policy_name:
                description:
                  - Policy used by Default Key
                type: str
          key_to_track_mappings:
            description:
              - Representing tracks needs separate content key
            type: list
            suboptions:
              label:
                description:
                  - >-
                    Label can be used to specify Content Key when creating a
                    Streaming Locator
                type: str
              policy_name:
                description:
                  - Policy used by Content Key
                type: str
              tracks:
                description:
                  - Tracks which use this content key
                type: list
                suboptions:
                  track_selections:
                    description:
                      - >-
                        TrackSelections is a track property condition list which
                        can specify track(s)
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
      custom_key_acquisition_url_template:
        description:
          - >-
            Template for the URL of the custom service delivering keys to end
            user players.  Not required when using Azure Media Services for
            issuing keys.  The template supports replaceable tokens that the
            service will update at runtime with the value specific to the
            request.  The currently supported token values are
            {AlternativeMediaId}, which is replaced with the value of
            StreamingLocatorId.AlternativeMediaId, and {ContentKeyId}, which is
            replaced with the value of identifier of the key being requested.
        type: str
  common_encryption_cenc:
    description:
      - Configuration of CommonEncryptionCenc
    type: dict
    suboptions:
      enabled_protocols:
        description:
          - Representing supported protocols
        type: dict
        suboptions:
          download:
            description:
              - Enable Download protocol or not
            required: true
            type: bool
          dash:
            description:
              - Enable DASH protocol or not
            required: true
            type: bool
          hls:
            description:
              - Enable HLS protocol or not
            required: true
            type: bool
          smooth_streaming:
            description:
              - Enable SmoothStreaming protocol or not
            required: true
            type: bool
      clear_tracks:
        description:
          - Representing which tracks should not be encrypted
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
      content_keys:
        description:
          - >-
            Representing default content key for each encryption scheme and
            separate content keys for specific tracks
        type: dict
        suboptions:
          default_key:
            description:
              - Default content key for an encryption scheme
            type: dict
            suboptions:
              label:
                description:
                  - >-
                    Label can be used to specify Content Key when creating a
                    Streaming Locator
                type: str
              policy_name:
                description:
                  - Policy used by Default Key
                type: str
          key_to_track_mappings:
            description:
              - Representing tracks needs separate content key
            type: list
            suboptions:
              label:
                description:
                  - >-
                    Label can be used to specify Content Key when creating a
                    Streaming Locator
                type: str
              policy_name:
                description:
                  - Policy used by Content Key
                type: str
              tracks:
                description:
                  - Tracks which use this content key
                type: list
                suboptions:
                  track_selections:
                    description:
                      - >-
                        TrackSelections is a track property condition list which
                        can specify track(s)
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
      drm:
        description:
          - Configuration of DRMs for CommonEncryptionCenc encryption scheme
        type: dict
        suboptions:
          play_ready:
            description:
              - PlayReady configurations
            type: dict
            suboptions:
              custom_license_acquisition_url_template:
                description:
                  - >-
                    Template for the URL of the custom service delivering
                    licenses to end user players.  Not required when using Azure
                    Media Services for issuing licenses.  The template supports
                    replaceable tokens that the service will update at runtime
                    with the value specific to the request.  The currently
                    supported token values are {AlternativeMediaId}, which is
                    replaced with the value of
                    StreamingLocatorId.AlternativeMediaId, and {ContentKeyId},
                    which is replaced with the value of identifier of the key
                    being requested.
                type: str
              play_ready_custom_attributes:
                description:
                  - Custom attributes for PlayReady
                type: str
          widevine:
            description:
              - Widevine configurations
            type: dict
            suboptions:
              custom_license_acquisition_url_template:
                description:
                  - >-
                    Template for the URL of the custom service delivering
                    licenses to end user players.  Not required when using Azure
                    Media Services for issuing licenses.  The template supports
                    replaceable tokens that the service will update at runtime
                    with the value specific to the request.  The currently
                    supported token values are {AlternativeMediaId}, which is
                    replaced with the value of
                    StreamingLocatorId.AlternativeMediaId, and {ContentKeyId},
                    which is replaced with the value of identifier of the key
                    being requested.
                type: str
  common_encryption_cbcs:
    description:
      - Configuration of CommonEncryptionCbcs
    type: dict
    suboptions:
      enabled_protocols:
        description:
          - Representing supported protocols
        type: dict
        suboptions:
          download:
            description:
              - Enable Download protocol or not
            required: true
            type: bool
          dash:
            description:
              - Enable DASH protocol or not
            required: true
            type: bool
          hls:
            description:
              - Enable HLS protocol or not
            required: true
            type: bool
          smooth_streaming:
            description:
              - Enable SmoothStreaming protocol or not
            required: true
            type: bool
      clear_tracks:
        description:
          - Representing which tracks should not be encrypted
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
      content_keys:
        description:
          - >-
            Representing default content key for each encryption scheme and
            separate content keys for specific tracks
        type: dict
        suboptions:
          default_key:
            description:
              - Default content key for an encryption scheme
            type: dict
            suboptions:
              label:
                description:
                  - >-
                    Label can be used to specify Content Key when creating a
                    Streaming Locator
                type: str
              policy_name:
                description:
                  - Policy used by Default Key
                type: str
          key_to_track_mappings:
            description:
              - Representing tracks needs separate content key
            type: list
            suboptions:
              label:
                description:
                  - >-
                    Label can be used to specify Content Key when creating a
                    Streaming Locator
                type: str
              policy_name:
                description:
                  - Policy used by Content Key
                type: str
              tracks:
                description:
                  - Tracks which use this content key
                type: list
                suboptions:
                  track_selections:
                    description:
                      - >-
                        TrackSelections is a track property condition list which
                        can specify track(s)
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
      drm:
        description:
          - Configuration of DRMs for current encryption scheme
        type: dict
        suboptions:
          fair_play:
            description:
              - FairPlay configurations
            type: dict
            suboptions:
              custom_license_acquisition_url_template:
                description:
                  - >-
                    Template for the URL of the custom service delivering
                    licenses to end user players.  Not required when using Azure
                    Media Services for issuing licenses.  The template supports
                    replaceable tokens that the service will update at runtime
                    with the value specific to the request.  The currently
                    supported token values are {AlternativeMediaId}, which is
                    replaced with the value of
                    StreamingLocatorId.AlternativeMediaId, and {ContentKeyId},
                    which is replaced with the value of identifier of the key
                    being requested.
                type: str
              allow_persistent_license:
                description:
                  - All license to be persistent or not
                required: true
                type: bool
          play_ready:
            description:
              - PlayReady configurations
            type: dict
            suboptions:
              custom_license_acquisition_url_template:
                description:
                  - >-
                    Template for the URL of the custom service delivering
                    licenses to end user players.  Not required when using Azure
                    Media Services for issuing licenses.  The template supports
                    replaceable tokens that the service will update at runtime
                    with the value specific to the request.  The currently
                    supported token values are {AlternativeMediaId}, which is
                    replaced with the value of
                    StreamingLocatorId.AlternativeMediaId, and {ContentKeyId},
                    which is replaced with the value of identifier of the key
                    being requested.
                type: str
              play_ready_custom_attributes:
                description:
                  - Custom attributes for PlayReady
                type: str
          widevine:
            description:
              - Widevine configurations
            type: dict
            suboptions:
              custom_license_acquisition_url_template:
                description:
                  - >-
                    Template for the URL of the custom service delivering
                    licenses to end user players.  Not required when using Azure
                    Media Services for issuing licenses.  The template supports
                    replaceable tokens that the service will update at runtime
                    with the value specific to the request.  The currently
                    supported token values are {AlternativeMediaId}, which is
                    replaced with the value of
                    StreamingLocatorId.AlternativeMediaId, and {ContentKeyId},
                    which is replaced with the value of identifier of the key
                    being requested.
                type: str
  no_encryption:
    description:
      - Configurations of NoEncryption
    type: dict
    suboptions:
      enabled_protocols:
        description:
          - Representing supported protocols
        type: dict
        suboptions:
          download:
            description:
              - Enable Download protocol or not
            required: true
            type: bool
          dash:
            description:
              - Enable DASH protocol or not
            required: true
            type: bool
          hls:
            description:
              - Enable HLS protocol or not
            required: true
            type: bool
          smooth_streaming:
            description:
              - Enable SmoothStreaming protocol or not
            required: true
            type: bool
  state:
    description:
      - Assert the state of the StreamingPolicy.
      - >-
        Use C(present) to create or update an StreamingPolicy and C(absent) to
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
    - name: Creates a Streaming Policy with clear streaming
      azure_rm_streamingpolicy: 
        account_name: contosomedia
        resource_group_name: contoso
        streaming_policy_name: UserCreatedClearStreamingPolicy
        properties:
          no_encryption:
            enabled_protocols:
              dash: true
              download: true
              hls: true
              smooth_streaming: true
        

    - name: Creates a Streaming Policy with commonEncryptionCbcs only
      azure_rm_streamingpolicy: 
        account_name: contosomedia
        resource_group_name: contoso
        streaming_policy_name: UserCreatedSecureStreamingPolicyWithCommonEncryptionCbcsOnly
        properties:
          common_encryption_cbcs:
            content_keys:
              default_key:
                label: cbcsDefaultKey
            drm:
              fair_play:
                allow_persistent_license: true
                custom_license_acquisition_url_template: 'https://contoso.com/{AssetAlternativeId}/fairplay/{ContentKeyId}'
            enabled_protocols:
              dash: false
              download: false
              hls: true
              smooth_streaming: false
          default_content_key_policy_name: PolicyWithMultipleOptions
        

    - name: Creates a Streaming Policy with commonEncryptionCenc only
      azure_rm_streamingpolicy: 
        account_name: contosomedia
        resource_group_name: contoso
        streaming_policy_name: UserCreatedSecureStreamingPolicyWithCommonEncryptionCencOnly
        properties:
          common_encryption_cenc:
            clear_tracks:
              - track_selections:
                  - operation: Equal
                    property: FourCC
                    value: hev1
            content_keys:
              default_key:
                label: cencDefaultKey
            drm:
              play_ready:
                custom_license_acquisition_url_template: 'https://contoso.com/{AssetAlternativeId}/playready/{ContentKeyId}'
                play_ready_custom_attributes: PlayReady CustomAttributes
              widevine:
                custom_license_acquisition_url_template: 'https://contoso.com/{AssetAlternativeId}/widevine/{ContentKeyId'
            enabled_protocols:
              dash: true
              download: false
              hls: false
              smooth_streaming: true
          default_content_key_policy_name: PolicyWithPlayReadyOptionAndOpenRestriction
        

    - name: Creates a Streaming Policy with envelopeEncryption only
      azure_rm_streamingpolicy: 
        account_name: contosomedia
        resource_group_name: contoso
        streaming_policy_name: UserCreatedSecureStreamingPolicyWithEnvelopeEncryptionOnly
        properties:
          default_content_key_policy_name: PolicyWithClearKeyOptionAndTokenRestriction
          envelope_encryption:
            content_keys:
              default_key:
                label: aesDefaultKey
            custom_key_acquisition_url_template: 'https://contoso.com/{AssetAlternativeId}/envelope/{ContentKeyId}'
            enabled_protocols:
              dash: true
              download: false
              hls: true
              smooth_streaming: true
        

    - name: Creates a Streaming Policy with secure streaming
      azure_rm_streamingpolicy: 
        account_name: contosomedia
        resource_group_name: contoso
        streaming_policy_name: UserCreatedSecureStreamingPolicy
        properties:
          common_encryption_cbcs:
            content_keys:
              default_key:
                label: cbcsDefaultKey
            drm:
              fair_play:
                allow_persistent_license: true
                custom_license_acquisition_url_template: 'https://contoso.com/{AssetAlternativeId}/fairplay/{ContentKeyId}'
            enabled_protocols:
              dash: false
              download: false
              hls: true
              smooth_streaming: false
          common_encryption_cenc:
            clear_tracks:
              - track_selections:
                  - operation: Equal
                    property: FourCC
                    value: hev1
            content_keys:
              default_key:
                label: cencDefaultKey
            drm:
              play_ready:
                custom_license_acquisition_url_template: 'https://contoso.com/{AssetAlternativeId}/playready/{ContentKeyId}'
                play_ready_custom_attributes: PlayReady CustomAttributes
              widevine:
                custom_license_acquisition_url_template: 'https://contoso.com/{AssetAlternativeId}/widevine/{ContentKeyId'
            enabled_protocols:
              dash: true
              download: false
              hls: false
              smooth_streaming: true
          default_content_key_policy_name: PolicyWithMultipleOptions
          envelope_encryption:
            content_keys:
              default_key:
                label: aesDefaultKey
            custom_key_acquisition_url_template: 'https://contoso.com/{AssetAlternativeId}/envelope/{ContentKeyId}'
            enabled_protocols:
              dash: true
              download: false
              hls: true
              smooth_streaming: true
        

    - name: Delete a Streaming Policy
      azure_rm_streamingpolicy: 
        account_name: contosomedia
        resource_group_name: contoso
        streaming_policy_name: secureStreamingPolicyWithCommonEncryptionCbcsOnly
        

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
    custom_key_acquisition_url_template:
      description:
        - >-
          Template for the URL of the custom service delivering keys to end user
          players.  Not required when using Azure Media Services for issuing
          keys.  The template supports replaceable tokens that the service will
          update at runtime with the value specific to the request.  The
          currently supported token values are {AlternativeMediaId}, which is
          replaced with the value of StreamingLocatorId.AlternativeMediaId, and
          {ContentKeyId}, which is replaced with the value of identifier of the
          key being requested.
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
                  Template for the URL of the custom service delivering licenses
                  to end user players.  Not required when using Azure Media
                  Services for issuing licenses.  The template supports
                  replaceable tokens that the service will update at runtime
                  with the value specific to the request.  The currently
                  supported token values are {AlternativeMediaId}, which is
                  replaced with the value of
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
                  Template for the URL of the custom service delivering licenses
                  to end user players.  Not required when using Azure Media
                  Services for issuing licenses.  The template supports
                  replaceable tokens that the service will update at runtime
                  with the value specific to the request.  The currently
                  supported token values are {AlternativeMediaId}, which is
                  replaced with the value of
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
                  Template for the URL of the custom service delivering licenses
                  to end user players.  Not required when using Azure Media
                  Services for issuing licenses.  The template supports
                  replaceable tokens that the service will update at runtime
                  with the value specific to the request.  The currently
                  supported token values are {AlternativeMediaId}, which is
                  replaced with the value of
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
                  Template for the URL of the custom service delivering licenses
                  to end user players.  Not required when using Azure Media
                  Services for issuing licenses.  The template supports
                  replaceable tokens that the service will update at runtime
                  with the value specific to the request.  The currently
                  supported token values are {AlternativeMediaId}, which is
                  replaced with the value of
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
                  Template for the URL of the custom service delivering licenses
                  to end user players.  Not required when using Azure Media
                  Services for issuing licenses.  The template supports
                  replaceable tokens that the service will update at runtime
                  with the value specific to the request.  The currently
                  supported token values are {AlternativeMediaId}, which is
                  replaced with the value of
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


class AzureRMStreamingPolicy(AzureRMModuleBaseExt):
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
            streaming_policy_name=dict(
                type='str',
                required=True
            ),
            default_content_key_policy_name=dict(
                type='str',
                disposition='/default_content_key_policy_name'
            ),
            envelope_encryption=dict(
                type='dict',
                disposition='/envelope_encryption',
                options=dict(
                    enabled_protocols=dict(
                        type='dict',
                        disposition='enabled_protocols',
                        options=dict(
                            download=dict(
                                type='bool',
                                disposition='download',
                                required=True
                            ),
                            dash=dict(
                                type='bool',
                                disposition='dash',
                                required=True
                            ),
                            hls=dict(
                                type='bool',
                                disposition='hls',
                                required=True
                            ),
                            smooth_streaming=dict(
                                type='bool',
                                disposition='smooth_streaming',
                                required=True
                            )
                        )
                    ),
                    clear_tracks=dict(
                        type='list',
                        disposition='clear_tracks',
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
                    ),
                    content_keys=dict(
                        type='dict',
                        disposition='content_keys',
                        options=dict(
                            default_key=dict(
                                type='dict',
                                disposition='default_key',
                                options=dict(
                                    label=dict(
                                        type='str',
                                        disposition='label'
                                    ),
                                    policy_name=dict(
                                        type='str',
                                        disposition='policy_name'
                                    )
                                )
                            ),
                            key_to_track_mappings=dict(
                                type='list',
                                disposition='key_to_track_mappings',
                                elements='dict',
                                options=dict(
                                    label=dict(
                                        type='str',
                                        disposition='label'
                                    ),
                                    policy_name=dict(
                                        type='str',
                                        disposition='policy_name'
                                    ),
                                    tracks=dict(
                                        type='list',
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
                            )
                        )
                    ),
                    custom_key_acquisition_url_template=dict(
                        type='str',
                        disposition='custom_key_acquisition_url_template'
                    )
                )
            ),
            common_encryption_cenc=dict(
                type='dict',
                disposition='/common_encryption_cenc',
                options=dict(
                    enabled_protocols=dict(
                        type='dict',
                        disposition='enabled_protocols',
                        options=dict(
                            download=dict(
                                type='bool',
                                disposition='download',
                                required=True
                            ),
                            dash=dict(
                                type='bool',
                                disposition='dash',
                                required=True
                            ),
                            hls=dict(
                                type='bool',
                                disposition='hls',
                                required=True
                            ),
                            smooth_streaming=dict(
                                type='bool',
                                disposition='smooth_streaming',
                                required=True
                            )
                        )
                    ),
                    clear_tracks=dict(
                        type='list',
                        disposition='clear_tracks',
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
                    ),
                    content_keys=dict(
                        type='dict',
                        disposition='content_keys',
                        options=dict(
                            default_key=dict(
                                type='dict',
                                disposition='default_key',
                                options=dict(
                                    label=dict(
                                        type='str',
                                        disposition='label'
                                    ),
                                    policy_name=dict(
                                        type='str',
                                        disposition='policy_name'
                                    )
                                )
                            ),
                            key_to_track_mappings=dict(
                                type='list',
                                disposition='key_to_track_mappings',
                                elements='dict',
                                options=dict(
                                    label=dict(
                                        type='str',
                                        disposition='label'
                                    ),
                                    policy_name=dict(
                                        type='str',
                                        disposition='policy_name'
                                    ),
                                    tracks=dict(
                                        type='list',
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
                            )
                        )
                    ),
                    drm=dict(
                        type='dict',
                        disposition='drm',
                        options=dict(
                            play_ready=dict(
                                type='dict',
                                disposition='play_ready',
                                options=dict(
                                    custom_license_acquisition_url_template=dict(
                                        type='str',
                                        disposition='custom_license_acquisition_url_template'
                                    ),
                                    play_ready_custom_attributes=dict(
                                        type='str',
                                        disposition='play_ready_custom_attributes'
                                    )
                                )
                            ),
                            widevine=dict(
                                type='dict',
                                disposition='widevine',
                                options=dict(
                                    custom_license_acquisition_url_template=dict(
                                        type='str',
                                        disposition='custom_license_acquisition_url_template'
                                    )
                                )
                            )
                        )
                    )
                )
            ),
            common_encryption_cbcs=dict(
                type='dict',
                disposition='/common_encryption_cbcs',
                options=dict(
                    enabled_protocols=dict(
                        type='dict',
                        disposition='enabled_protocols',
                        options=dict(
                            download=dict(
                                type='bool',
                                disposition='download',
                                required=True
                            ),
                            dash=dict(
                                type='bool',
                                disposition='dash',
                                required=True
                            ),
                            hls=dict(
                                type='bool',
                                disposition='hls',
                                required=True
                            ),
                            smooth_streaming=dict(
                                type='bool',
                                disposition='smooth_streaming',
                                required=True
                            )
                        )
                    ),
                    clear_tracks=dict(
                        type='list',
                        disposition='clear_tracks',
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
                    ),
                    content_keys=dict(
                        type='dict',
                        disposition='content_keys',
                        options=dict(
                            default_key=dict(
                                type='dict',
                                disposition='default_key',
                                options=dict(
                                    label=dict(
                                        type='str',
                                        disposition='label'
                                    ),
                                    policy_name=dict(
                                        type='str',
                                        disposition='policy_name'
                                    )
                                )
                            ),
                            key_to_track_mappings=dict(
                                type='list',
                                disposition='key_to_track_mappings',
                                elements='dict',
                                options=dict(
                                    label=dict(
                                        type='str',
                                        disposition='label'
                                    ),
                                    policy_name=dict(
                                        type='str',
                                        disposition='policy_name'
                                    ),
                                    tracks=dict(
                                        type='list',
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
                            )
                        )
                    ),
                    drm=dict(
                        type='dict',
                        disposition='drm',
                        options=dict(
                            fair_play=dict(
                                type='dict',
                                disposition='fair_play',
                                options=dict(
                                    custom_license_acquisition_url_template=dict(
                                        type='str',
                                        disposition='custom_license_acquisition_url_template'
                                    ),
                                    allow_persistent_license=dict(
                                        type='bool',
                                        disposition='allow_persistent_license',
                                        required=True
                                    )
                                )
                            ),
                            play_ready=dict(
                                type='dict',
                                disposition='play_ready',
                                options=dict(
                                    custom_license_acquisition_url_template=dict(
                                        type='str',
                                        disposition='custom_license_acquisition_url_template'
                                    ),
                                    play_ready_custom_attributes=dict(
                                        type='str',
                                        disposition='play_ready_custom_attributes'
                                    )
                                )
                            ),
                            widevine=dict(
                                type='dict',
                                disposition='widevine',
                                options=dict(
                                    custom_license_acquisition_url_template=dict(
                                        type='str',
                                        disposition='custom_license_acquisition_url_template'
                                    )
                                )
                            )
                        )
                    )
                )
            ),
            no_encryption=dict(
                type='dict',
                disposition='/no_encryption',
                options=dict(
                    enabled_protocols=dict(
                        type='dict',
                        disposition='enabled_protocols',
                        options=dict(
                            download=dict(
                                type='bool',
                                disposition='download',
                                required=True
                            ),
                            dash=dict(
                                type='bool',
                                disposition='dash',
                                required=True
                            ),
                            hls=dict(
                                type='bool',
                                disposition='hls',
                                required=True
                            ),
                            smooth_streaming=dict(
                                type='bool',
                                disposition='smooth_streaming',
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
        self.streaming_policy_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMStreamingPolicy, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                response = self.mgmt_client.streaming_policies.create(resource_group_name=self.resource_group_name,
                                                                      account_name=self.account_name,
                                                                      streaming_policy_name=self.streaming_policy_name,
                                                                      parameters=self.body)
            else:
                response = self.mgmt_client.streaming_policies.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the StreamingPolicy instance.')
            self.fail('Error creating the StreamingPolicy instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.streaming_policies.delete(resource_group_name=self.resource_group_name,
                                                                  account_name=self.account_name,
                                                                  streaming_policy_name=self.streaming_policy_name)
        except CloudError as e:
            self.log('Error attempting to delete the StreamingPolicy instance.')
            self.fail('Error deleting the StreamingPolicy instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.streaming_policies.get(resource_group_name=self.resource_group_name,
                                                               account_name=self.account_name,
                                                               streaming_policy_name=self.streaming_policy_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMStreamingPolicy()


if __name__ == '__main__':
    main()
