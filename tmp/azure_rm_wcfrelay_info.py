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
module: azure_rm_wcfrelay_info
version_added: '2.9'
short_description: Get WCFRelay info.
description:
  - Get info of WCFRelay.
options:
  resource_group_name:
    description:
      - Name of the Resource group within the Azure subscription.
    required: true
    type: str
  namespace_name:
    description:
      - The namespace name
    required: true
    type: str
  relay_name:
    description:
      - The relay name.
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
    - name: RelayListAll
      azure_rm_wcfrelay_info: 
        namespace_name: sdk-RelayNamespace-01
        resource_group_name: RG-eg
        

    - name: RelayGet
      azure_rm_wcfrelay_info: 
        namespace_name: sdk-RelayNamespace-9953
        relay_name: sdk-Relay-Wcf-1194
        resource_group_name: RG-eg
        

    - name: RelayAutorizationRuleListAll
      azure_rm_wcfrelay_info: 
        namespace_name: sdk-RelayNamespace-01
        relay_name: sdk-Relay-Wcf-01
        resource_group_name: RG-eg
        

    - name: RelayAutorizationRuleGet
      azure_rm_wcfrelay_info: 
        authorization_rule_name: sdk-RelayAuthRules-01
        namespace_name: sdk-RelayNamespace-01
        relay_name: sdk-Relay-wcf-01
        resource_group_name: RG-eg
        

'''

RETURN = '''
wcfrelays:
  description: >-
    A list of dict results where the key is the name of the WCFRelay and the
    values are the facts for that WCFRelay.
  returned: always
  type: complex
  contains:
    value:
      description:
        - |-
          Result of the list WCF relay operation.
          Result of the list authorization rules operation.
      returned: always
      type: list
      sample: null
      contains:
        is_dynamic:
          description:
            - 'Returns true if the relay is dynamic; otherwise, false.'
          returned: always
          type: bool
          sample: null
        created_at:
          description:
            - The time the WCF relay was created.
          returned: always
          type: str
          sample: null
        updated_at:
          description:
            - The time the namespace was updated.
          returned: always
          type: str
          sample: null
        listener_count:
          description:
            - >-
              The number of listeners for this relay. Note that min :1 and
              max:25 are supported.
          returned: always
          type: integer
          sample: null
        relay_type:
          description:
            - WCF relay type.
          returned: always
          type: sealed-choice
          sample: null
        requires_client_authorization:
          description:
            - >-
              Returns true if client authorization is needed for this relay;
              otherwise, false.
          returned: always
          type: bool
          sample: null
        requires_transport_security:
          description:
            - >-
              Returns true if transport security is needed for this relay;
              otherwise, false.
          returned: always
          type: bool
          sample: null
        user_metadata:
          description:
            - >-
              The usermetadata is a placeholder to store user-defined string
              data for the WCF Relay endpoint. For example, it can be used to
              store descriptive data, such as list of teams and their contact
              information. Also, user-defined configuration settings can be
              stored.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - >-
          Link to the next set of results. Not empty if value contains
          incomplete list of WCF relays.

          Link to the next set of results. Not empty if value contains
          incomplete list of authorization rules.
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
    is_dynamic:
      description:
        - 'Returns true if the relay is dynamic; otherwise, false.'
      returned: always
      type: bool
      sample: null
    created_at:
      description:
        - The time the WCF relay was created.
      returned: always
      type: str
      sample: null
    updated_at:
      description:
        - The time the namespace was updated.
      returned: always
      type: str
      sample: null
    listener_count:
      description:
        - >-
          The number of listeners for this relay. Note that min :1 and max:25
          are supported.
      returned: always
      type: integer
      sample: null
    relay_type:
      description:
        - WCF relay type.
      returned: always
      type: sealed-choice
      sample: null
    requires_client_authorization:
      description:
        - >-
          Returns true if client authorization is needed for this relay;
          otherwise, false.
      returned: always
      type: bool
      sample: null
    requires_transport_security:
      description:
        - >-
          Returns true if transport security is needed for this relay;
          otherwise, false.
      returned: always
      type: bool
      sample: null
    user_metadata:
      description:
        - >-
          The usermetadata is a placeholder to store user-defined string data
          for the WCF Relay endpoint. For example, it can be used to store
          descriptive data, such as list of teams and their contact information.
          Also, user-defined configuration settings can be stored.
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
    from azure.mgmt.relay import Relay API
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMWCFRelayInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            namespace_name=dict(
                type='str',
                required=True
            ),
            relay_name=dict(
                type='str'
            ),
            authorization_rule_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.namespace_name = None
        self.relay_name = None
        self.authorization_rule_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMWCFRelayInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Relay API,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-04-01')

        if (self.resource_group_name is not None and
            self.namespace_name is not None and
            self.relay_name is not None and
            self.authorization_rule_name is not None):
            self.results['wcfrelays'] = self.format_item(self.getauthorizationrule())
        elif (self.resource_group_name is not None and
              self.namespace_name is not None and
              self.relay_name is not None):
            self.results['wcfrelays'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.namespace_name is not None and
              self.relay_name is not None):
            self.results['wcfrelays'] = self.format_item(self.listauthorizationrule())
        elif (self.resource_group_name is not None and
              self.namespace_name is not None):
            self.results['wcfrelays'] = self.format_item(self.listbynamespace())
        return self.results

    def getauthorizationrule(self):
        response = None

        try:
            response = self.mgmt_client.wcfrelays.get_authorization_rule(resource_group_name=self.resource_group_name,
                                                                         namespace_name=self.namespace_name,
                                                                         relay_name=self.relay_name,
                                                                         authorization_rule_name=self.authorization_rule_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def get(self):
        response = None

        try:
            response = self.mgmt_client.wcfrelays.get(resource_group_name=self.resource_group_name,
                                                      namespace_name=self.namespace_name,
                                                      relay_name=self.relay_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listauthorizationrule(self):
        response = None

        try:
            response = self.mgmt_client.wcfrelays.list_authorization_rule(resource_group_name=self.resource_group_name,
                                                                          namespace_name=self.namespace_name,
                                                                          relay_name=self.relay_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbynamespace(self):
        response = None

        try:
            response = self.mgmt_client.wcfrelays.list_by_namespace(resource_group_name=self.resource_group_name,
                                                                    namespace_name=self.namespace_name)
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
    AzureRMWCFRelayInfo()


if __name__ == '__main__':
    main()
