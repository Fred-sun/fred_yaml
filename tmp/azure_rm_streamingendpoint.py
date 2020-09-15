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
module: azure_rm_streamingendpoint
version_added: '2.9'
short_description: Manage Azure StreamingEndpoint instance.
description:
  - 'Create, update and delete instance of Azure StreamingEndpoint.'
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
  streaming_endpoint_name:
    description:
      - The name of the StreamingEndpoint.
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
      - The StreamingEndpoint description.
    type: str
  scale_units:
    description:
      - >-
        The number of scale units.  Use the Scale operation to adjust this
        value.
    type: integer
  availability_set_name:
    description:
      - >-
        The name of the AvailabilitySet used with this StreamingEndpoint for
        high availability streaming.  This value can only be set at creation
        time.
    type: str
  max_cache_age:
    description:
      - Max cache age
    type: integer
  custom_host_names:
    description:
      - The custom host names of the StreamingEndpoint
    type: list
  cdn_enabled:
    description:
      - The CDN enabled flag.
    type: bool
  cdn_provider:
    description:
      - The CDN provider name.
    type: str
  cdn_profile:
    description:
      - The CDN profile name.
    type: str
  cross_site_access_policies:
    description:
      - The StreamingEndpoint access policies.
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
  akamai:
    description:
      - The access control of Akamai
    type: dict
    suboptions:
      akamai_signature_header_authentication_key_list:
        description:
          - authentication key list
        type: list
        suboptions:
          identifier:
            description:
              - identifier of the key
            type: str
          base64key:
            description:
              - authentication key
            type: str
          expiration:
            description:
              - The expiration time of the authentication key.
            type: str
  ip:
    description:
      - The IP access control of the StreamingEndpoint.
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
  state:
    description:
      - Assert the state of the StreamingEndpoint.
      - >-
        Use C(present) to create or update an StreamingEndpoint and C(absent) to
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
    - name: Create a StreamingEndpoint
      azure_rm_streamingendpoint: 
        account_name: slitestmedia10
        resource_group_name: mediaresources
        streaming_endpoint_name: myStreamingEndpoint1
        id: {}
        location: West US
        properties:
          description: test event 1
          access_control:
            akamai:
              akamai_signature_header_authentication_key_list:
                - base64key: dGVzdGlkMQ==
                  expiration: '2029-12-31T16:00:00-08:00'
                  identifier: id1
                - base64key: dGVzdGlkMQ==
                  expiration: '2030-12-31T16:00:00-08:00'
                  identifier: id2
            ip:
              allow:
                - name: AllowedIp
                  address: 192.168.1.1
          availability_set_name: availableset
          cdn_enabled: false
          scale_units: 1
        tags:
          tag1: value1
          tag2: value2
        

    - name: Update a StreamingEndpoint
      azure_rm_streamingendpoint: 
        account_name: slitestmedia10
        resource_group_name: mediaresources
        streaming_endpoint_name: myStreamingEndpoint1
        id: {}
        location: West US
        properties:
          description: test event 2
          availability_set_name: availableset
          scale_units: 5
        tags:
          tag3: value3
          tag5: value5
        

    - name: Delete a StreamingEndpoint
      azure_rm_streamingendpoint: 
        account_name: slitestmedia10
        resource_group_name: mediaresources
        streaming_endpoint_name: myStreamingEndpoint1
        location: West US
        name: myStreamingEndpoint1
        tags:
          dynamic_properties:
            tag1: value1
            tag2: value2
        type: >-
          /subscriptions/0a6ec948-5a62-437d-b9df-934dc7c1b722/resourcegroups/mediaresources/providers/Microsoft.Media/mediaservices/slitestmedia10/streamingendpoints
        id: >-
          /subscriptions/0a6ec948-5a62-437d-b9df-934dc7c1b722/resourceGroups/mediaresources/providers/Microsoft.Media/mediaservices/slitestmedia10/streamingendpoints/myStreamingEndpoint1
        properties:
          access_control: {}
          availability_set_name: availableset
          cdn_enabled: false
          cdn_profile: {}
          cdn_provider: {}
          created: '2018-03-02T18:25:09.4897514-08:00'
          cross_site_access_policies: {}
          custom_host_names: []
          description: test event 1
          free_trial_end_time: '0001-01-01T00:00:00-08:00'
          host_name: {}
          last_modified: '2018-03-02T18:25:09.4897514-08:00'
          max_cache_age: {}
          provisioning_state: {}
          resource_state: Stopped
          scale_units: 1
        

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
    - The StreamingEndpoint description.
  returned: always
  type: str
  sample: null
scale_units:
  description:
    - The number of scale units.  Use the Scale operation to adjust this value.
  returned: always
  type: integer
  sample: null
availability_set_name:
  description:
    - >-
      The name of the AvailabilitySet used with this StreamingEndpoint for high
      availability streaming.  This value can only be set at creation time.
  returned: always
  type: str
  sample: null
max_cache_age:
  description:
    - Max cache age
  returned: always
  type: integer
  sample: null
custom_host_names:
  description:
    - The custom host names of the StreamingEndpoint
  returned: always
  type: list
  sample: null
host_name:
  description:
    - The StreamingEndpoint host name.
  returned: always
  type: str
  sample: null
cdn_enabled:
  description:
    - The CDN enabled flag.
  returned: always
  type: bool
  sample: null
cdn_provider:
  description:
    - The CDN provider name.
  returned: always
  type: str
  sample: null
cdn_profile:
  description:
    - The CDN profile name.
  returned: always
  type: str
  sample: null
provisioning_state:
  description:
    - The provisioning state of the StreamingEndpoint.
  returned: always
  type: str
  sample: null
resource_state:
  description:
    - The resource state of the StreamingEndpoint.
  returned: always
  type: str
  sample: null
cross_site_access_policies:
  description:
    - The StreamingEndpoint access policies.
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
free_trial_end_time:
  description:
    - The free trial expiration time.
  returned: always
  type: str
  sample: null
created:
  description:
    - The exact time the StreamingEndpoint was created.
  returned: always
  type: str
  sample: null
last_modified:
  description:
    - The exact time the StreamingEndpoint was last modified.
  returned: always
  type: str
  sample: null
akamai:
  description:
    - The access control of Akamai
  returned: always
  type: dict
  sample: null
  contains:
    akamai_signature_header_authentication_key_list:
      description:
        - authentication key list
      returned: always
      type: list
      sample: null
      contains:
        identifier:
          description:
            - identifier of the key
          returned: always
          type: str
          sample: null
        base64key:
          description:
            - authentication key
          returned: always
          type: str
          sample: null
        expiration:
          description:
            - The expiration time of the authentication key.
          returned: always
          type: str
          sample: null
ip:
  description:
    - The IP access control of the StreamingEndpoint.
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


class AzureRMStreamingEndpoint(AzureRMModuleBaseExt):
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
            streaming_endpoint_name=dict(
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
            scale_units=dict(
                type='integer',
                disposition='/scale_units'
            ),
            availability_set_name=dict(
                type='str',
                disposition='/availability_set_name'
            ),
            max_cache_age=dict(
                type='integer',
                disposition='/max_cache_age'
            ),
            custom_host_names=dict(
                type='list',
                disposition='/custom_host_names',
                elements='str'
            ),
            cdn_enabled=dict(
                type='bool',
                disposition='/cdn_enabled'
            ),
            cdn_provider=dict(
                type='str',
                disposition='/cdn_provider'
            ),
            cdn_profile=dict(
                type='str',
                disposition='/cdn_profile'
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
            akamai=dict(
                type='dict',
                disposition='/akamai',
                options=dict(
                    akamai_signature_header_authentication_key_list=dict(
                        type='list',
                        disposition='akamai_signature_header_authentication_key_list',
                        elements='dict',
                        options=dict(
                            identifier=dict(
                                type='str',
                                disposition='identifier'
                            ),
                            base64key=dict(
                                type='str',
                                disposition='base64key'
                            ),
                            expiration=dict(
                                type='str',
                                disposition='expiration'
                            )
                        )
                    )
                )
            ),
            ip=dict(
                type='dict',
                disposition='/ip',
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
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.streaming_endpoint_name = None
        self.auto_start = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMStreamingEndpoint, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                response = self.mgmt_client.streaming_endpoints.create(resource_group_name=self.resource_group_name,
                                                                       account_name=self.account_name,
                                                                       streaming_endpoint_name=self.streaming_endpoint_name,
                                                                       auto_start=self.auto_start,
                                                                       parameters=self.body)
            else:
                response = self.mgmt_client.streaming_endpoints.update(resource_group_name=self.resource_group_name,
                                                                       account_name=self.account_name,
                                                                       streaming_endpoint_name=self.streaming_endpoint_name,
                                                                       parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the StreamingEndpoint instance.')
            self.fail('Error creating the StreamingEndpoint instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.streaming_endpoints.delete(resource_group_name=self.resource_group_name,
                                                                   account_name=self.account_name,
                                                                   streaming_endpoint_name=self.streaming_endpoint_name)
        except CloudError as e:
            self.log('Error attempting to delete the StreamingEndpoint instance.')
            self.fail('Error deleting the StreamingEndpoint instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.streaming_endpoints.get(resource_group_name=self.resource_group_name,
                                                                account_name=self.account_name,
                                                                streaming_endpoint_name=self.streaming_endpoint_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMStreamingEndpoint()


if __name__ == '__main__':
    main()
