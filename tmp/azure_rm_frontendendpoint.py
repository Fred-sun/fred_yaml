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
module: azure_rm_frontendendpoint
version_added: '2.9'
short_description: Manage Azure FrontendEndpoint instance.
description:
  - 'Create, update and delete instance of Azure FrontendEndpoint.'
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
    required: true
    type: str
  state:
    description:
      - Assert the state of the FrontendEndpoint.
      - >-
        Use C(present) to create or update an FrontendEndpoint and C(absent) to
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
'''

RETURN = '''
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
      UNUSED. This field will be ignored. The TTL to use in seconds for session
      affinity, if applicable.
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
        - Defines the TLS extension protocol that is used for secure delivery
      returned: always
      type: str
      sample: null
    minimum_tls_version:
      description:
        - >-
          The minimum TLS version required from the clients to establish an SSL
          handshake with Front Door.
      returned: always
      type: str
      sample: null
    certificate_type:
      description:
        - >-
          Defines the type of the certificate used for secure connections to a
          frontendEndpoint
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
        - The name of the Key Vault secret representing the full certificate PFX
      returned: always
      type: str
      sample: null
    secret_version:
      description:
        - >-
          The version of the Key Vault secret representing the full certificate
          PFX
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
    from azure.mgmt.front import FrontDoorManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMFrontendEndpoint(AzureRMModuleBaseExt):
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
                type='str',
                required=True
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.front_door_name = None
        self.frontend_endpoint_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMFrontendEndpoint, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(FrontDoorManagementClient,
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
                response = self.mgmt_client.frontend_endpoints.create()
            else:
                response = self.mgmt_client.frontend_endpoints.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the FrontendEndpoint instance.')
            self.fail('Error creating the FrontendEndpoint instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.frontend_endpoints.delete()
        except CloudError as e:
            self.log('Error attempting to delete the FrontendEndpoint instance.')
            self.fail('Error deleting the FrontendEndpoint instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.frontend_endpoints.get(resource_group_name=self.resource_group_name,
                                                               front_door_name=self.front_door_name,
                                                               frontend_endpoint_name=self.frontend_endpoint_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMFrontendEndpoint()


if __name__ == '__main__':
    main()
