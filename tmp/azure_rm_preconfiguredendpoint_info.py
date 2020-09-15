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
module: azure_rm_preconfiguredendpoint_info
version_added: '2.9'
short_description: Get PreconfiguredEndpoint info.
description:
  - Get info of PreconfiguredEndpoint.
options:
  resource_group_name:
    description:
      - Name of the Resource group within the Azure subscription.
    required: true
    type: str
  profile_name:
    description:
      - The Profile identifier associated with the Tenant and Partner
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Gets a list of Preconfigured Endpoints
      azure_rm_preconfiguredendpoint_info: 
        profile_name: MyProfile
        resource_group_name: MyResourceGroup
        

'''

RETURN = '''
preconfigured_endpoints:
  description: >-
    A list of dict results where the key is the name of the
    PreconfiguredEndpoint and the values are the facts for that
    PreconfiguredEndpoint.
  returned: always
  type: complex
  contains:
    value:
      description:
        - List of PreconfiguredEndpoints supported by NetworkExperiment.
      returned: always
      type: list
      sample: null
      contains:
        description:
          description:
            - The description of the endpoint
          returned: always
          type: str
          sample: null
        endpoint:
          description:
            - The endpoint that is preconfigured
          returned: always
          type: str
          sample: null
        endpoint_type:
          description:
            - The type of endpoint
          returned: always
          type: str
          sample: null
        backend:
          description:
            - The preconfigured endpoint backend
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - URL to get the next set of PreconfiguredEndpoints if there are any.
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


class AzureRMPreconfiguredEndpointInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            profile_name=dict(
                type='str',
                required=True
            )
        )

        self.resource_group_name = None
        self.profile_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-11-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMPreconfiguredEndpointInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(FrontDoorManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-11-01')

        if (self.resource_group_name is not None and
            self.profile_name is not None):
            self.results['preconfigured_endpoints'] = self.format_item(self.list())
        return self.results

    def list(self):
        response = None

        try:
            response = self.mgmt_client.preconfigured_endpoints.list(resource_group_name=self.resource_group_name,
                                                                     profile_name=self.profile_name)
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
    AzureRMPreconfiguredEndpointInfo()


if __name__ == '__main__':
    main()
