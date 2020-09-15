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
module: azure_rm_contentkeypolicy_info
version_added: '2.9'
short_description: Get ContentKeyPolicy info.
description:
  - Get info of ContentKeyPolicy.
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
  content_key_policy_name:
    description:
      - The Content Key Policy name.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Lists Content Key Policies ordered by last modified.
      azure_rm_contentkeypolicy_info: 
        account_name: contosomedia
        resource_group_name: contoso
        

    - name: Lists Content Key Policies with created and last modified filters.
      azure_rm_contentkeypolicy_info: 
        account_name: contosomedia
        resource_group_name: contoso
        

    - name: Lists all Content Key Policies
      azure_rm_contentkeypolicy_info: 
        account_name: contosomedia
        resource_group_name: contoso
        

    - name: Get a Content Key Policy by name
      azure_rm_contentkeypolicy_info: 
        account_name: contosomedia
        content_key_policy_name: PolicyWithMultipleOptions
        resource_group_name: contoso
        

'''

RETURN = '''
content_key_policies:
  description: >-
    A list of dict results where the key is the name of the ContentKeyPolicy and
    the values are the facts for that ContentKeyPolicy.
  returned: always
  type: complex
  contains:
    value:
      description:
        - A collection of ContentKeyPolicy items.
      returned: always
      type: list
      sample: null
      contains:
        policy_id:
          description:
            - The legacy Policy ID.
          returned: always
          type: uuid
          sample: null
        created:
          description:
            - The creation date of the Policy
          returned: always
          type: str
          sample: null
        last_modified:
          description:
            - The last modified date of the Policy
          returned: always
          type: str
          sample: null
        description:
          description:
            - A description for the Policy.
          returned: always
          type: str
          sample: null
        options:
          description:
            - The Key Policy options.
          returned: always
          type: list
          sample: null
          contains:
            policy_option_id:
              description:
                - The legacy Policy Option ID.
              returned: always
              type: uuid
              sample: null
            name:
              description:
                - The Policy Option description.
              returned: always
              type: str
              sample: null
            configuration:
              description:
                - The key delivery configuration.
              returned: always
              type: dict
              sample: null
              contains:
                odata_type:
                  description:
                    - The discriminator for derived types.
                  returned: always
                  type: str
                  sample: null
            restriction:
              description:
                - >-
                  The requirements that must be met to deliver keys with this
                  configuration
              returned: always
              type: dict
              sample: null
              contains:
                odata_type:
                  description:
                    - The discriminator for derived types.
                  returned: always
                  type: str
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
    policy_id:
      description:
        - The legacy Policy ID.
      returned: always
      type: uuid
      sample: null
    created:
      description:
        - The creation date of the Policy
      returned: always
      type: str
      sample: null
    last_modified:
      description:
        - The last modified date of the Policy
      returned: always
      type: str
      sample: null
    description:
      description:
        - A description for the Policy.
      returned: always
      type: str
      sample: null
    options:
      description:
        - The Key Policy options.
      returned: always
      type: list
      sample: null
      contains:
        policy_option_id:
          description:
            - The legacy Policy Option ID.
          returned: always
          type: uuid
          sample: null
        name:
          description:
            - The Policy Option description.
          returned: always
          type: str
          sample: null
        configuration:
          description:
            - The key delivery configuration.
          returned: always
          type: dict
          sample: null
          contains:
            odata_type:
              description:
                - The discriminator for derived types.
              returned: always
              type: str
              sample: null
        restriction:
          description:
            - >-
              The requirements that must be met to deliver keys with this
              configuration
          returned: always
          type: dict
          sample: null
          contains:
            odata_type:
              description:
                - The discriminator for derived types.
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
    from azure.mgmt.azure import Azure Media Services
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMContentKeyPolicyInfo(AzureRMModuleBase):
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
            content_key_policy_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.filter = None
        self.top = None
        self.orderby = None
        self.content_key_policy_name = None

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
        super(AzureRMContentKeyPolicyInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Azure Media Services,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-05-01')

        if (self.resource_group_name is not None and
            self.account_name is not None and
            self.content_key_policy_name is not None):
            self.results['content_key_policies'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.account_name is not None):
            self.results['content_key_policies'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.content_key_policies.get(resource_group_name=self.resource_group_name,
                                                                 account_name=self.account_name,
                                                                 content_key_policy_name=self.content_key_policy_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.content_key_policies.list(resource_group_name=self.resource_group_name,
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
    AzureRMContentKeyPolicyInfo()


if __name__ == '__main__':
    main()
