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
module: azure_rm_domain
version_added: '2.9'
short_description: Manage Azure Domain instance.
description:
  - 'Create, update and delete instance of Azure Domain.'
options:
  resource_group_name:
    description:
      - The name of the resource group within the user's subscription.
    required: true
    type: str
  domain_name:
    description:
      - Name of the domain.
    required: true
    type: str
  location:
    description:
      - Location of the resource.
    type: str
  private_endpoint_connections:
    description:
      - List of private endpoint connections.
    type: list
    suboptions:
      group_ids:
        description:
          - GroupIds from the private link service resource.
        type: list
      private_link_service_connection_state:
        description:
          - Details about the state of the connection.
        type: dict
        suboptions:
          status:
            description:
              - Status of the connection.
            type: str
            choices:
              - Pending
              - Approved
              - Rejected
              - Disconnected
          description:
            description:
              - Description of the connection state.
            type: str
          actions_required:
            description:
              - Actions required (if any).
            type: str
      provisioning_state:
        description:
          - Provisioning state of the Private Endpoint Connection.
        type: str
        choices:
          - Creating
          - Updating
          - Deleting
          - Succeeded
          - Canceled
          - Failed
      id_properties_private_endpoint_id:
        description:
          - The ARM identifier for Private Endpoint.
        type: str
  input_schema:
    description:
      - >-
        This determines the format that Event Grid should expect for incoming
        events published to the domain.
    type: str
    choices:
      - EventGridSchema
      - CustomEventSchema
      - CloudEventSchemaV1_0
  input_schema_mapping:
    description:
      - >-
        Information about the InputSchemaMapping which specified the info about
        mapping event payload.
    type: dict
    suboptions:
      input_schema_mapping_type:
        description:
          - Type of the custom mapping
        required: true
        type: str
        choices:
          - Json
  public_network_access:
    description:
      - "This determines if traffic is allowed over public network. By default it is enabled. \r"
      - >-
        You can further restrict to specific IPs by configuring <seealso
        cref="P:Microsoft.Azure.Events.ResourceProvider.Common.Contracts.DomainProperties.InboundIpRules"
        />
      - "This determines if traffic is allowed over public network. By default it is enabled. \r"
      - >-
        You can further restrict to specific IPs by configuring <seealso
        cref="P:Microsoft.Azure.Events.ResourceProvider.Common.Contracts.DomainUpdateParameterProperties.InboundIpRules"
        />
    type: str
    choices:
      - Enabled
      - Disabled
  inbound_ip_rules:
    description:
      - >-
        This can be used to restrict traffic from specific IPs instead of all
        IPs. Note: These are considered only if PublicNetworkAccess is enabled.
    type: list
    suboptions:
      ip_mask:
        description:
          - 'IP Address in CIDR notation e.g., 10.0.0.0/8.'
        type: str
      action:
        description:
          - Action to perform based on the match or no match of the IpMask.
        type: str
        choices:
          - Allow
  state:
    description:
      - Assert the state of the Domain.
      - Use C(present) to create or update an Domain and C(absent) to delete it.
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
    - name: Domains_CreateOrUpdate
      azure_rm_domain: 
        domain_name: exampledomain1
        resource_group_name: examplerg
        

    - name: Domains_Delete
      azure_rm_domain: 
        domain_name: exampledomain1
        resource_group_name: examplerg
        

    - name: Domains_Update
      azure_rm_domain: 
        domain_name: exampledomain1
        resource_group_name: examplerg
        

'''

RETURN = '''
location:
  description:
    - Location of the resource.
  returned: always
  type: str
  sample: null
tags:
  description:
    - Tags of the resource.
  returned: always
  type: dictionary
  sample: null
private_endpoint_connections:
  description:
    - List of private endpoint connections.
  returned: always
  type: list
  sample: null
  contains:
    group_ids:
      description:
        - GroupIds from the private link service resource.
      returned: always
      type: list
      sample: null
    private_link_service_connection_state:
      description:
        - Details about the state of the connection.
      returned: always
      type: dict
      sample: null
      contains:
        status:
          description:
            - Status of the connection.
          returned: always
          type: str
          sample: null
        description:
          description:
            - Description of the connection state.
          returned: always
          type: str
          sample: null
        actions_required:
          description:
            - Actions required (if any).
          returned: always
          type: str
          sample: null
    provisioning_state:
      description:
        - Provisioning state of the Private Endpoint Connection.
      returned: always
      type: str
      sample: null
    id_properties_private_endpoint_id:
      description:
        - The ARM identifier for Private Endpoint.
      returned: always
      type: str
      sample: null
provisioning_state:
  description:
    - Provisioning state of the domain.
  returned: always
  type: str
  sample: null
endpoint:
  description:
    - Endpoint for the domain.
  returned: always
  type: str
  sample: null
input_schema:
  description:
    - >-
      This determines the format that Event Grid should expect for incoming
      events published to the domain.
  returned: always
  type: str
  sample: null
input_schema_mapping:
  description:
    - >-
      Information about the InputSchemaMapping which specified the info about
      mapping event payload.
  returned: always
  type: dict
  sample: null
  contains:
    input_schema_mapping_type:
      description:
        - Type of the custom mapping
      returned: always
      type: str
      sample: null
metric_resource_id:
  description:
    - Metric resource id for the domain.
  returned: always
  type: str
  sample: null
public_network_access:
  description:
    - "This determines if traffic is allowed over public network. By default it is enabled. \r\nYou can further restrict to specific IPs by configuring <seealso cref=\"P:Microsoft.Azure.Events.ResourceProvider.Common.Contracts.DomainProperties.InboundIpRules\" />"
  returned: always
  type: str
  sample: null
inbound_ip_rules:
  description:
    - >-
      This can be used to restrict traffic from specific IPs instead of all IPs.
      Note: These are considered only if PublicNetworkAccess is enabled.
  returned: always
  type: list
  sample: null
  contains:
    ip_mask:
      description:
        - 'IP Address in CIDR notation e.g., 10.0.0.0/8.'
      returned: always
      type: str
      sample: null
    action:
      description:
        - Action to perform based on the match or no match of the IpMask.
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
    from azure.mgmt.event import EventGridManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMDomain(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            domain_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            private_endpoint_connections=dict(
                type='list',
                disposition='/private_endpoint_connections',
                elements='dict',
                options=dict(
                    group_ids=dict(
                        type='list',
                        disposition='group_ids',
                        elements='str'
                    ),
                    private_link_service_connection_state=dict(
                        type='dict',
                        disposition='private_link_service_connection_state',
                        options=dict(
                            status=dict(
                                type='str',
                                disposition='status',
                                choices=['Pending',
                                         'Approved',
                                         'Rejected',
                                         'Disconnected']
                            ),
                            description=dict(
                                type='str',
                                disposition='description'
                            ),
                            actions_required=dict(
                                type='str',
                                disposition='actions_required'
                            )
                        )
                    ),
                    provisioning_state=dict(
                        type='str',
                        disposition='provisioning_state',
                        choices=['Creating',
                                 'Updating',
                                 'Deleting',
                                 'Succeeded',
                                 'Canceled',
                                 'Failed']
                    ),
                    id_properties_private_endpoint_id=dict(
                        type='str',
                        disposition='id_properties_private_endpoint_id'
                    )
                )
            ),
            input_schema=dict(
                type='str',
                disposition='/input_schema',
                choices=['EventGridSchema',
                         'CustomEventSchema',
                         'CloudEventSchemaV1_0']
            ),
            input_schema_mapping=dict(
                type='dict',
                disposition='/input_schema_mapping',
                options=dict(
                    input_schema_mapping_type=dict(
                        type='str',
                        disposition='input_schema_mapping_type',
                        choices=['Json'],
                        required=True
                    )
                )
            ),
            public_network_access=dict(
                type='str',
                disposition='/public_network_access',
                choices=['Enabled',
                         'Disabled']
            ),
            inbound_ip_rules=dict(
                type='list',
                disposition='/inbound_ip_rules',
                elements='dict',
                options=dict(
                    ip_mask=dict(
                        type='str',
                        disposition='ip_mask'
                    ),
                    action=dict(
                        type='str',
                        disposition='action',
                        choices=['Allow']
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
        self.domain_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMDomain, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(EventGridManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

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
            response = self.mgmt_client.domains.create_or_update(resource_group_name=self.resource_group_name,
                                                                 domain_name=self.domain_name,
                                                                 domain_info=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Domain instance.')
            self.fail('Error creating the Domain instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.domains.delete(resource_group_name=self.resource_group_name,
                                                       domain_name=self.domain_name)
        except CloudError as e:
            self.log('Error attempting to delete the Domain instance.')
            self.fail('Error deleting the Domain instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.domains.get(resource_group_name=self.resource_group_name,
                                                    domain_name=self.domain_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMDomain()


if __name__ == '__main__':
    main()
