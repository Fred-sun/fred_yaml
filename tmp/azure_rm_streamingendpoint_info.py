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
module: azure_rm_streamingendpoint_info
version_added: '2.9'
short_description: Get StreamingEndpoint info.
description:
  - Get info of StreamingEndpoint.
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
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List all StreamingEndpoints
      azure_rm_streamingendpoint_info: 
        account_name: slitestmedia10
        resource_group_name: mediaresources
        

    - name: Get a StreamingEndpoint by name
      azure_rm_streamingendpoint_info: 
        account_name: slitestmedia10
        resource_group_name: mediaresources
        streaming_endpoint_name: myStreamingEndpoint1
        

'''

RETURN = '''
streaming_endpoints:
  description: >-
    A list of dict results where the key is the name of the StreamingEndpoint
    and the values are the facts for that StreamingEndpoint.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The result of the List StreamingEndpoint operation.
      returned: always
      type: list
      sample: null
      contains:
        description:
          description:
            - The StreamingEndpoint description.
          returned: always
          type: str
          sample: null
        scale_units:
          description:
            - >-
              The number of scale units.  Use the Scale operation to adjust this
              value.
          returned: always
          type: integer
          sample: null
        availability_set_name:
          description:
            - >-
              The name of the AvailabilitySet used with this StreamingEndpoint
              for high availability streaming.  This value can only be set at
              creation time.
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
          incomplete list of StreamingEndpoints.
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
        - The StreamingEndpoint description.
      returned: always
      type: str
      sample: null
    scale_units:
      description:
        - >-
          The number of scale units.  Use the Scale operation to adjust this
          value.
      returned: always
      type: integer
      sample: null
    availability_set_name:
      description:
        - >-
          The name of the AvailabilitySet used with this StreamingEndpoint for
          high availability streaming.  This value can only be set at creation
          time.
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


class AzureRMStreamingEndpointInfo(AzureRMModuleBase):
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
                type='str'
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.streaming_endpoint_name = None

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
        super(AzureRMStreamingEndpointInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Azure Media Services,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-05-01')

        if (self.resource_group_name is not None and
            self.account_name is not None and
            self.streaming_endpoint_name is not None):
            self.results['streaming_endpoints'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.account_name is not None):
            self.results['streaming_endpoints'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.streaming_endpoints.get(resource_group_name=self.resource_group_name,
                                                                account_name=self.account_name,
                                                                streaming_endpoint_name=self.streaming_endpoint_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.streaming_endpoints.list(resource_group_name=self.resource_group_name,
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
    AzureRMStreamingEndpointInfo()


if __name__ == '__main__':
    main()
