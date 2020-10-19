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
module: azure_rm_frontendendpoint_info
version_added: '2.9'
short_description: Get FrontendEndpoint info.
description:
  - Get info of FrontendEndpoint.
options:
  resource_group_name:
    description:
      - Name of the Resource group within the Azure subscription.
    required: true
    type: str
  front_door_name:
    description:
      - Name of the Front Door which is globally unique.
    required: true
    type: str
  frontend_endpoint_name:
    description:
      - Name of the Frontend endpoint which is unique within the Front Door.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List Frontend endpoints in a Front Door
      azure_rm_frontendendpoint_info: 
        front_door_name: frontDoor1
        resource_group_name: rg1
        

    - name: Get Frontend Endpoint
      azure_rm_frontendendpoint_info: 
        front_door_name: frontDoor1
        frontend_endpoint_name: frontendEndpoint1
        resource_group_name: rg1
        

'''

RETURN = '''
frontend_endpoints:
  description: >-
    A list of dict results where the key is the name of the FrontendEndpoint and
    the values are the facts for that FrontendEndpoint.
  returned: always
  type: complex
  contains:
    value:
      description:
        - List of Frontend endpoints within a Front Door.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - Resource name.
          returned: always
          type: str
          sample: null
        type:
          description:
            - Resource type.
          returned: always
          type: str
          sample: null
        host_name:
          description:
            - The host name of the frontendEndpoint. Must be a domain name.
          returned: always
          type: str
          sample: null
        session_affinity_enabled_state:
          description:
            - >-
              Whether to allow session affinity on this host. Valid options are
              'Enabled' or 'Disabled'
          returned: always
          type: str
          sample: null
        session_affinity_ttl_seconds:
          description:
            - >-
              UNUSED. This field will be ignored. The TTL to use in seconds for
              session affinity, if applicable.
          returned: always
          type: integer
          sample: null
        id_properties_web_application_firewall_policy_link_id:
          description:
            - Resource ID.
          returned: always
          type: str
          sample: null
        resource_state:
          description:
            - Resource status.
          returned: always
          type: str
          sample: null
        custom_https_provisioning_state:
          description:
            - Provisioning status of Custom Https of the frontendEndpoint.
          returned: always
          type: str
          sample: null
        custom_https_provisioning_substate:
          description:
            - >-
              Provisioning substate shows the progress of custom HTTPS
              enabling/disabling process step by step.
          returned: always
          type: str
          sample: null
        custom_https_configuration:
          description:
            - The configuration specifying how to enable HTTPS
          returned: always
          type: dict
          sample: null
          contains:
            certificate_source:
              description:
                - Defines the source of the SSL certificate
              returned: always
              type: str
              sample: null
            protocol_type:
              description:
                - >-
                  Defines the TLS extension protocol that is used for secure
                  delivery
              returned: always
              type: str
              sample: null
            minimum_tls_version:
              description:
                - >-
                  The minimum TLS version required from the clients to establish
                  an SSL handshake with Front Door.
              returned: always
              type: str
              sample: null
            certificate_type:
              description:
                - >-
                  Defines the type of the certificate used for secure
                  connections to a frontendEndpoint
              returned: always
              type: str
              sample: null
            vault:
              description:
                - The Key Vault containing the SSL certificate
              returned: always
              type: dict
              sample: null
              contains:
                id:
                  description:
                    - Resource ID.
                  returned: always
                  type: str
                  sample: null
            secret_name:
              description:
                - >-
                  The name of the Key Vault secret representing the full
                  certificate PFX
              returned: always
              type: str
              sample: null
            secret_version:
              description:
                - >-
                  The version of the Key Vault secret representing the full
                  certificate PFX
              returned: always
              type: str
              sample: null
    next_link:
      description:
        - URL to get the next set of frontend endpoints if there are any.
      returned: always
      type: str
      sample: null
    id:
      description:
        - Resource ID.
      returned: always
      type: str
      sample: null
    name:
      description:
        - Resource name.
      returned: always
      type: str
      sample: null
    type:
      description:
        - Resource type.
      returned: always
      type: str
      sample: null
    host_name:
      description:
        - The host name of the frontendEndpoint. Must be a domain name.
      returned: always
      type: str
      sample: null
    session_affinity_enabled_state:
      description:
        - >-
          Whether to allow session affinity on this host. Valid options are
          'Enabled' or 'Disabled'
      returned: always
      type: str
      sample: null
    session_affinity_ttl_seconds:
      description:
        - >-
          UNUSED. This field will be ignored. The TTL to use in seconds for
          session affinity, if applicable.
      returned: always
      type: integer
      sample: null
    id_properties_web_application_firewall_policy_link_id:
      description:
        - Resource ID.
      returned: always
      type: str
      sample: null
    resource_state:
      description:
        - Resource status.
      returned: always
      type: str
      sample: null
    custom_https_provisioning_state:
      description:
        - Provisioning status of Custom Https of the frontendEndpoint.
      returned: always
      type: str
      sample: null
    custom_https_provisioning_substate:
      description:
        - >-
          Provisioning substate shows the progress of custom HTTPS
          enabling/disabling process step by step.
      returned: always
      type: str
      sample: null
    custom_https_configuration:
      description:
        - The configuration specifying how to enable HTTPS
      returned: always
      type: dict
      sample: null
      contains:
        certificate_source:
          description:
            - Defines the source of the SSL certificate
          returned: always
          type: str
          sample: null
        protocol_type:
          description:
            - >-
              Defines the TLS extension protocol that is used for secure
              delivery
          returned: always
          type: str
          sample: null
        minimum_tls_version:
          description:
            - >-
              The minimum TLS version required from the clients to establish an
              SSL handshake with Front Door.
          returned: always
          type: str
          sample: null
        certificate_type:
          description:
            - >-
              Defines the type of the certificate used for secure connections to
              a frontendEndpoint
          returned: always
          type: str
          sample: null
        vault:
          description:
            - The Key Vault containing the SSL certificate
          returned: always
          type: dict
          sample: null
          contains:
            id:
              description:
                - Resource ID.
              returned: always
              type: str
              sample: null
        secret_name:
          description:
            - >-
              The name of the Key Vault secret representing the full certificate
              PFX
          returned: always
          type: str
          sample: null
        secret_version:
          description:
            - >-
              The version of the Key Vault secret representing the full
              certificate PFX
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
    from azure.mgmt.front import FrontDoorManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMFrontendEndpointInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            front_door_name=dict(
                type='str',
                required=True
            ),
            frontend_endpoint_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.front_door_name = None
        self.frontend_endpoint_name = None

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
        super(AzureRMFrontendEndpointInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(FrontDoorManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-05-01')

        if (self.resource_group_name is not None and
            self.front_door_name is not None and
            self.frontend_endpoint_name is not None):
            self.results['frontend_endpoints'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.front_door_name is not None):
            self.results['frontend_endpoints'] = self.format_item(self.listbyfrontdoor())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.frontend_endpoints.get(resource_group_name=self.resource_group_name,
                                                               front_door_name=self.front_door_name,
                                                               frontend_endpoint_name=self.frontend_endpoint_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyfrontdoor(self):
        response = None

        try:
            response = self.mgmt_client.frontend_endpoints.list_by_front_door(resource_group_name=self.resource_group_name,
                                                                              front_door_name=self.front_door_name)
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
    AzureRMFrontendEndpointInfo()


if __name__ == '__main__':
    main()
