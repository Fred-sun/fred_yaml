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
module: azure_rm_userassignedidentity_info
version_added: '2.9'
short_description: Get UserAssignedIdentity info.
description:
  - Get info of UserAssignedIdentity.
options:
  resource_group_name:
    description:
      - The name of the Resource Group to which the identity belongs.
    type: str
  resource_name:
    description:
      - The name of the identity resource.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: IdentityListBySubscription
      azure_rm_userassignedidentity_info: 
        {}
        

    - name: IdentityListByResourceGroup
      azure_rm_userassignedidentity_info: 
        resource_group_name: rgName
        

    - name: IdentityGet
      azure_rm_userassignedidentity_info: 
        resource_group_name: rgName
        resource_name: resourceName
        

'''

RETURN = '''
user_assigned_identities:
  description: >-
    A list of dict results where the key is the name of the UserAssignedIdentity
    and the values are the facts for that UserAssignedIdentity.
  returned: always
  type: complex
  contains:
    value:
      description:
        - >-
          The collection of userAssignedIdentities returned by the listing
          operation.
      returned: always
      type: list
      sample: null
      contains:
        tenant_id:
          description:
            - The id of the tenant which the identity belongs to.
          returned: always
          type: uuid
          sample: null
        principal_id:
          description:
            - >-
              The id of the service principal object associated with the created
              identity.
          returned: always
          type: uuid
          sample: null
        client_id:
          description:
            - >-
              The id of the app associated with the identity. This is a random
              generated UUID by MSI.
          returned: always
          type: uuid
          sample: null
    next_link:
      description:
        - 'The url to get the next page of results, if any.'
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
    tenant_id:
      description:
        - The id of the tenant which the identity belongs to.
      returned: always
      type: uuid
      sample: null
    principal_id:
      description:
        - >-
          The id of the service principal object associated with the created
          identity.
      returned: always
      type: uuid
      sample: null
    client_id:
      description:
        - >-
          The id of the app associated with the identity. This is a random
          generated UUID by MSI.
      returned: always
      type: uuid
      sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.managed import ManagedServiceIdentityClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMUserAssignedIdentityInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            resource_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.resource_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-11-30'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMUserAssignedIdentityInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ManagedServiceIdentityClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-11-30')

        if (self.resource_group_name is not None and
            self.resource_name is not None):
            self.results['user_assigned_identities'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['user_assigned_identities'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['user_assigned_identities'] = self.format_item(self.listbysubscription())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.user_assigned_identities.get(resource_group_name=self.resource_group_name,
                                                                     resource_name=self.resource_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.user_assigned_identities.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbysubscription(self):
        response = None

        try:
            response = self.mgmt_client.user_assigned_identities.list_by_subscription()
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
    AzureRMUserAssignedIdentityInfo()


if __name__ == '__main__':
    main()
