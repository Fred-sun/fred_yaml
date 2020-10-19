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
module: azure_rm_systemassignedidentity_info
version_added: '2.9'
short_description: Get SystemAssignedIdentity info.
description:
  - Get info of SystemAssignedIdentity.
options:
  scope:
    description:
      - >-
        The resource provider scope of the resource. Parent resource being
        extended by Managed Identities.
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: MsiOperationsList
      azure_rm_systemassignedidentity_info: 
        scope: scope
        

'''

RETURN = '''
system_assigned_identities:
  description: >-
    A list of dict results where the key is the name of the
    SystemAssignedIdentity and the values are the facts for that
    SystemAssignedIdentity.
  returned: always
  type: complex
  contains:
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
    location:
      description:
        - The geo-location where the resource lives
      returned: always
      type: str
      sample: null
    tags:
      description:
        - Resource tags
      returned: always
      type: dictionary
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
    client_secret_url:
      description:
        - ' The ManagedServiceIdentity DataPlane URL that can be queried to obtain the identity credentials.'
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
    from azure.mgmt.managed import ManagedServiceIdentityClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMSystemAssignedIdentityInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            scope=dict(
                type='str',
                required=True
            )
        )

        self.scope = None

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
        super(AzureRMSystemAssignedIdentityInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ManagedServiceIdentityClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-11-30')

        if (self.scope is not None):
            self.results['system_assigned_identities'] = self.format_item(self.getbyscope())
        return self.results

    def getbyscope(self):
        response = None

        try:
            response = self.mgmt_client.system_assigned_identities.get_by_scope(scope=self.scope)
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
    AzureRMSystemAssignedIdentityInfo()


if __name__ == '__main__':
    main()
