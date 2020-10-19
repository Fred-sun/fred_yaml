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
module: azure_rm_domain_info
version_added: '2.9'
short_description: Get Domain info.
description:
  - Get info of Domain.
options:
  resource_group_name:
    description:
      - The name of the resource group within the user's subscription.
    type: str
  domain_name:
    description:
      - Name of the domain.
    type: str
  filter:
    description:
      - >-
        The query used to filter the search results using OData syntax.
        Filtering is permitted on the 'name' property only and with limited
        number of OData operations. These operations are: the 'contains'
        function as well as the following logical operations: not, and, or, eq
        (for equal), and ne (for not equal). No arithmetic operations are
        supported. The following is a valid filter example:
        $filter=contains(namE, 'PATTERN') and name ne 'PATTERN-1'. The following
        is not a valid filter example: $filter=location eq 'westus'.
    type: str
  top:
    description:
      - >-
        The number of results to return per page for the list operation. Valid
        range for top parameter is 1 to 100. If not specified, the default
        number of results to be returned is 20 items per page.
    type: integer
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Domains_Get
      azure_rm_domain_info: 
        domain_name: exampledomain2
        resource_group_name: examplerg
        

    - name: Domains_ListBySubscription
      azure_rm_domain_info: 
        {}
        

    - name: Domains_ListByResourceGroup
      azure_rm_domain_info: 
        resource_group_name: examplerg
        

'''

RETURN = '''
domains:
  description: >-
    A list of dict results where the key is the name of the Domain and the
    values are the facts for that Domain.
  returned: always
  type: complex
  contains:
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
          Information about the InputSchemaMapping which specified the info
          about mapping event payload.
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
          This can be used to restrict traffic from specific IPs instead of all
          IPs. Note: These are considered only if PublicNetworkAccess is
          enabled.
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
    value:
      description:
        - A collection of Domains.
      returned: always
      type: list
      sample: null
      contains:
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
              This determines the format that Event Grid should expect for
              incoming events published to the domain.
          returned: always
          type: str
          sample: null
        input_schema_mapping:
          description:
            - >-
              Information about the InputSchemaMapping which specified the info
              about mapping event payload.
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
              This can be used to restrict traffic from specific IPs instead of
              all IPs. Note: These are considered only if PublicNetworkAccess is
              enabled.
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
                - >-
                  Action to perform based on the match or no match of the
                  IpMask.
              returned: always
              type: str
              sample: null
    next_link:
      description:
        - A link for the next page of domains.
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
    from azure.mgmt.event import EventGridManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMDomainInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            domain_name=dict(
                type='str'
            ),
            filter=dict(
                type='str'
            ),
            top=dict(
                type='integer'
            )
        )

        self.resource_group_name = None
        self.domain_name = None
        self.filter = None
        self.top = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-06-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMDomainInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(EventGridManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

        if (self.resource_group_name is not None and
            self.domain_name is not None):
            self.results['domains'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['domains'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['domains'] = self.format_item(self.listbysubscription())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.domains.get(resource_group_name=self.resource_group_name,
                                                    domain_name=self.domain_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.domains.list_by_resource_group(resource_group_name=self.resource_group_name,
                                                                       filter=self.filter,
                                                                       top=self.top)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbysubscription(self):
        response = None

        try:
            response = self.mgmt_client.domains.list_by_subscription(filter=self.filter,
                                                                     top=self.top)
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
    AzureRMDomainInfo()


if __name__ == '__main__':
    main()
