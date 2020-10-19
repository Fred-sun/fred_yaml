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
module: azure_rm_namespace_info
version_added: '2.9'
short_description: Get Namespace info.
description:
  - Get info of Namespace.
options:
  resource_group_name:
    description:
      - Name of the Resource group within the Azure subscription.
    type: str
  namespace_name:
    description:
      - The namespace name
    type: str
  ip_filter_rule_name:
    description:
      - The IP Filter Rule name.
    type: str
  virtual_network_rule_name:
    description:
      - The Virtual Network Rule name.
    type: str
  authorization_rule_name:
    description:
      - The authorization rule name.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: ListIpFilterRules
      azure_rm_namespace_info: 
        namespace_name: sdk-Namespace-5232
        resource_group_name: ResourceGroup
        

    - name: NameSpaceIpFilterRuleGet
      azure_rm_namespace_info: 
        ip_filter_rule_name: sdk-IPFilterRules-7337
        namespace_name: sdk-Namespace-5232
        resource_group_name: ResourceGroup
        

    - name: NameSpaceList
      azure_rm_namespace_info: 
        {}
        

    - name: NameSpaceListByResourceGroup
      azure_rm_namespace_info: 
        resource_group_name: ArunMonocle
        

    - name: NameSpaceGet
      azure_rm_namespace_info: 
        namespace_name: sdk-Namespace-2924
        resource_group_name: ArunMonocle
        

    - name: NameSpaceVirtualNetworkRuleSetget
      azure_rm_namespace_info: 
        namespace_name: sdk-Namespace-6019
        resource_group_name: ResourceGroup
        

    - name: NameSpaceVirtualNetworkRuleGet
      azure_rm_namespace_info: 
        namespace_name: sdk-Namespace-6019
        resource_group_name: ResourceGroup
        virtual_network_rule_name: sdk-VirtualNetworkRules-9191
        

    - name: NameSpaceAuthorizationRuleListAll
      azure_rm_namespace_info: 
        namespace_name: sdk-Namespace-6914
        resource_group_name: ArunMonocle
        

    - name: NameSpaceAuthorizationRuleGet
      azure_rm_namespace_info: 
        authorization_rule_name: sdk-AuthRules-1788
        namespace_name: sdk-Namespace-6914
        resource_group_name: ArunMonocle
        

'''

RETURN = '''
namespaces:
  description: >-
    A list of dict results where the key is the name of the Namespace and the
    values are the facts for that Namespace.
  returned: always
  type: complex
  contains:
    value:
      description:
        - |-
          Result of the List IpFilter Rules operation.
          Result of the List Namespace operation.
          Result of the List VirtualNetwork Rules operation.
          Result of the List Authorization Rules operation.
      returned: always
      type: list
      sample: null
      contains:
        ip_mask:
          description:
            - IP Mask
          returned: always
          type: str
          sample: null
        action:
          description:
            - The IP Filter Action
          returned: always
          type: str
          sample: null
        filter_name:
          description:
            - IP Filter name
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - >-
          Link to the next set of results. Not empty if Value contains an
          incomplete list of IpFilter Rules

          Link to the next set of results. Not empty if Value contains
          incomplete list of Namespaces.

          Link to the next set of results. Not empty if Value contains an
          incomplete list of VirtualNetwork Rules

          Link to the next set of results. Not empty if Value contains
          incomplete list of Authorization Rules.
      returned: always
      type: str
      sample: null
    id:
      description:
        - Resource Id
      returned: always
      type: str
      sample: null
    name:
      description:
        - Resource name
      returned: always
      type: str
      sample: null
    type:
      description:
        - Resource type
      returned: always
      type: str
      sample: null
    ip_mask:
      description:
        - IP Mask
      returned: always
      type: str
      sample: null
    action:
      description:
        - The IP Filter Action
      returned: always
      type: str
      sample: null
    filter_name:
      description:
        - IP Filter name
      returned: always
      type: str
      sample: null
    location:
      description:
        - The Geo-location where the resource lives
      returned: always
      type: str
      sample: null
    tags:
      description:
        - Resource tags
      returned: always
      type: dictionary
      sample: null
    sku:
      description:
        - Properties of SKU
      returned: always
      type: dict
      sample: null
      contains:
        name:
          description:
            - Name of this SKU.
          returned: always
          type: sealed-choice
          sample: null
        tier:
          description:
            - The billing tier of this particular SKU.
          returned: always
          type: sealed-choice
          sample: null
        capacity:
          description:
            - >-
              The specified messaging units for the tier. For Premium tier,
              capacity are 1,2 and 4.
          returned: always
          type: integer
          sample: null
    provisioning_state:
      description:
        - Provisioning state of the namespace.
      returned: always
      type: str
      sample: null
    created_at:
      description:
        - The time the namespace was created
      returned: always
      type: str
      sample: null
    updated_at:
      description:
        - The time the namespace was updated.
      returned: always
      type: str
      sample: null
    service_bus_endpoint:
      description:
        - Endpoint you can use to perform Service Bus operations.
      returned: always
      type: str
      sample: null
    metric_id:
      description:
        - Identifier for Azure Insights metrics
      returned: always
      type: str
      sample: null
    zone_redundant:
      description:
        - >-
          Enabling this property creates a Premium Service Bus Namespace in
          regions supported availability zones.
      returned: always
      type: bool
      sample: null
    key_vault_properties:
      description:
        - Properties of KeyVault
      returned: always
      type: dict
      sample: null
      contains:
        key_name:
          description:
            - Name of the Key from KeyVault
          returned: always
          type: str
          sample: null
        key_vault_uri:
          description:
            - Uri of KeyVault
          returned: always
          type: str
          sample: null
    key_source:
      description:
        - Enumerates the possible value of keySource for Encryption
      returned: always
      type: constant
      sample: null
    default_action:
      description:
        - Default Action for Network Rule Set
      returned: always
      type: str
      sample: null
    virtual_network_rules:
      description:
        - List VirtualNetwork Rules
      returned: always
      type: list
      sample: null
      contains:
        ignore_missing_vnet_service_endpoint:
          description:
            - >-
              Value that indicates whether to ignore missing Vnet Service
              Endpoint
          returned: always
          type: bool
          sample: null
        id:
          description:
            - Resource ID of Virtual Network Subnet
          returned: always
          type: str
          sample: null
    ip_rules:
      description:
        - List of IpRules
      returned: always
      type: list
      sample: null
      contains:
        ip_mask:
          description:
            - IP Mask
          returned: always
          type: str
          sample: null
        action:
          description:
            - The IP Filter Action
          returned: always
          type: str
          sample: null
    virtual_network_subnet_id:
      description:
        - Resource ID of Virtual Network Subnet
      returned: always
      type: str
      sample: null
    rights:
      description:
        - The rights associated with the rule.
      returned: always
      type: list
      sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.service import ServiceBusManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMNamespaceInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            namespace_name=dict(
                type='str'
            ),
            ip_filter_rule_name=dict(
                type='str'
            ),
            virtual_network_rule_name=dict(
                type='str'
            ),
            authorization_rule_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.namespace_name = None
        self.ip_filter_rule_name = None
        self.virtual_network_rule_name = None
        self.authorization_rule_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-01-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMNamespaceInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ServiceBusManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-01-01-preview')

        if (self.resource_group_name is not None and
            self.namespace_name is not None and
            self.ip_filter_rule_name is not None):
            self.results['namespaces'] = self.format_item(self.getipfilterrule())
        elif (self.resource_group_name is not None and
              self.namespace_name is not None and
              self.virtual_network_rule_name is not None):
            self.results['namespaces'] = self.format_item(self.getvirtualnetworkrule())
        elif (self.resource_group_name is not None and
              self.namespace_name is not None and
              self.authorization_rule_name is not None):
            self.results['namespaces'] = self.format_item(self.getauthorizationrule())
        elif (self.resource_group_name is not None and
              self.namespace_name is not None):
            self.results['namespaces'] = self.format_item(self.listipfilterrule())
        elif (self.resource_group_name is not None and
              self.namespace_name is not None):
            self.results['namespaces'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.namespace_name is not None):
            self.results['namespaces'] = self.format_item(self.getnetworkruleset())
        elif (self.resource_group_name is not None and
              self.namespace_name is not None):
            self.results['namespaces'] = self.format_item(self.listvirtualnetworkrule())
        elif (self.resource_group_name is not None and
              self.namespace_name is not None):
            self.results['namespaces'] = self.format_item(self.listauthorizationrule())
        elif (self.resource_group_name is not None):
            self.results['namespaces'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['namespaces'] = self.format_item(self.list())
        return self.results

    def getipfilterrule(self):
        response = None

        try:
            response = self.mgmt_client.namespaces.get_ip_filter_rule(resource_group_name=self.resource_group_name,
                                                                      namespace_name=self.namespace_name,
                                                                      ip_filter_rule_name=self.ip_filter_rule_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def getvirtualnetworkrule(self):
        response = None

        try:
            response = self.mgmt_client.namespaces.get_virtual_network_rule(resource_group_name=self.resource_group_name,
                                                                            namespace_name=self.namespace_name,
                                                                            virtual_network_rule_name=self.virtual_network_rule_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def getauthorizationrule(self):
        response = None

        try:
            response = self.mgmt_client.namespaces.get_authorization_rule(resource_group_name=self.resource_group_name,
                                                                          namespace_name=self.namespace_name,
                                                                          authorization_rule_name=self.authorization_rule_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listipfilterrule(self):
        response = None

        try:
            response = self.mgmt_client.namespaces.list_ip_filter_rule(resource_group_name=self.resource_group_name,
                                                                       namespace_name=self.namespace_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def get(self):
        response = None

        try:
            response = self.mgmt_client.namespaces.get(resource_group_name=self.resource_group_name,
                                                       namespace_name=self.namespace_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def getnetworkruleset(self):
        response = None

        try:
            response = self.mgmt_client.namespaces.get_network_rule_set(resource_group_name=self.resource_group_name,
                                                                        namespace_name=self.namespace_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listvirtualnetworkrule(self):
        response = None

        try:
            response = self.mgmt_client.namespaces.list_virtual_network_rule(resource_group_name=self.resource_group_name,
                                                                             namespace_name=self.namespace_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listauthorizationrule(self):
        response = None

        try:
            response = self.mgmt_client.namespaces.list_authorization_rule(resource_group_name=self.resource_group_name,
                                                                           namespace_name=self.namespace_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.namespaces.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.namespaces.list()
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
    AzureRMNamespaceInfo()


if __name__ == '__main__':
    main()
