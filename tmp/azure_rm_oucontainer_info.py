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
module: azure_rm_oucontainer_info
version_added: '2.9'
short_description: Get OuContainer info.
description:
  - Get info of OuContainer.
options:
  resource_group_name:
    description:
      - >-
        The name of the resource group within the user's subscription. The name
        is case insensitive.
    required: true
    type: str
  domain_service_name:
    description:
      - The name of the domain service.
    required: true
    type: str
  ou_container_name:
    description:
      - The name of the OuContainer.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List of OuContainers
      azure_rm_oucontainer_info: 
        domain_service_name: OuContainer.com
        resource_group_name: OuContainerResourceGroup
        

'''

RETURN = '''
ou_container:
  description: >-
    A list of dict results where the key is the name of the OuContainer and the
    values are the facts for that OuContainer.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The list of OuContainer.
      returned: always
      type: list
      sample: null
      contains:
        tenant_id:
          description:
            - Azure Active Directory tenant id
          returned: always
          type: str
          sample: null
        domain_name:
          description:
            - The domain name of Domain Services.
          returned: always
          type: str
          sample: null
        deployment_id:
          description:
            - The Deployment id
          returned: always
          type: str
          sample: null
        container_id:
          description:
            - The OuContainer name
          returned: always
          type: str
          sample: null
        accounts:
          description:
            - The list of container accounts
          returned: always
          type: list
          sample: null
          contains:
            account_name:
              description:
                - The account name
              returned: always
              type: str
              sample: null
            spn:
              description:
                - The account spn
              returned: always
              type: str
              sample: null
            password:
              description:
                - The account password
              returned: always
              type: str
              sample: null
        service_status:
          description:
            - Status of OuContainer instance
          returned: always
          type: str
          sample: null
        provisioning_state:
          description:
            - >-
              The current deployment or provisioning state, which only appears
              in the response.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - The continuation token for the next page of results.
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
    location:
      description:
        - Resource location
      returned: always
      type: str
      sample: null
    tags:
      description:
        - Resource tags
      returned: always
      type: dictionary
      sample: null
    etag:
      description:
        - Resource etag
      returned: always
      type: str
      sample: null
    tenant_id:
      description:
        - Azure Active Directory tenant id
      returned: always
      type: str
      sample: null
    domain_name:
      description:
        - The domain name of Domain Services.
      returned: always
      type: str
      sample: null
    deployment_id:
      description:
        - The Deployment id
      returned: always
      type: str
      sample: null
    container_id:
      description:
        - The OuContainer name
      returned: always
      type: str
      sample: null
    accounts:
      description:
        - The list of container accounts
      returned: always
      type: list
      sample: null
      contains:
        account_name:
          description:
            - The account name
          returned: always
          type: str
          sample: null
        spn:
          description:
            - The account spn
          returned: always
          type: str
          sample: null
        password:
          description:
            - The account password
          returned: always
          type: str
          sample: null
    service_status:
      description:
        - Status of OuContainer instance
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - >-
          The current deployment or provisioning state, which only appears in
          the response.
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
    from azure.mgmt.domain import Domain Services Resource Provider
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMOuContainerInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            domain_service_name=dict(
                type='str',
                required=True
            ),
            ou_container_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.domain_service_name = None
        self.ou_container_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-06-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMOuContainerInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Domain Services Resource Provider,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-06-01')

        if (self.resource_group_name is not None and
            self.domain_service_name is not None and
            self.ou_container_name is not None):
            self.results['ou_container'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.domain_service_name is not None):
            self.results['ou_container'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.ou_container.get(resource_group_name=self.resource_group_name,
                                                         domain_service_name=self.domain_service_name,
                                                         ou_container_name=self.ou_container_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.ou_container.list(resource_group_name=self.resource_group_name,
                                                          domain_service_name=self.domain_service_name)
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
    AzureRMOuContainerInfo()


if __name__ == '__main__':
    main()
