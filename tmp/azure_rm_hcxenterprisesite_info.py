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
module: azure_rm_hcxenterprisesite_info
version_added: '2.9'
short_description: Get HcxEnterpriseSite info.
description:
  - Get info of HcxEnterpriseSite.
options:
  resource_group_name:
    description:
      - The name of the resource group. The name is case insensitive.
    required: true
    type: str
  private_cloud_name:
    description:
      - Name of the private cloud
    required: true
    type: str
  hcx_enterprise_site_name:
    description:
      - Name of the HCX Enterprise Site in the private cloud
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: HcxEnterpriseSites_List
      azure_rm_hcxenterprisesite_info: 
        private_cloud_name: cloud1
        resource_group_name: group1
        

    - name: HcxEnterpriseSites_Get
      azure_rm_hcxenterprisesite_info: 
        hcx_enterprise_site_name: site1
        private_cloud_name: cloud1
        resource_group_name: group1
        

'''

RETURN = '''
hcx_enterprise_sites:
  description: >-
    A list of dict results where the key is the name of the HcxEnterpriseSite
    and the values are the facts for that HcxEnterpriseSite.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The items on a page
      returned: always
      type: list
      sample: null
      contains:
        activation_key:
          description:
            - The activation key
          returned: always
          type: str
          sample: null
        status:
          description:
            - The status of the HCX Enterprise Site
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - URL to get the next page if any
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
    activation_key:
      description:
        - The activation key
      returned: always
      type: str
      sample: null
    status:
      description:
        - The status of the HCX Enterprise Site
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
    from azure.mgmt.azure import Azure VMware Solution API
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMHcxEnterpriseSiteInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            private_cloud_name=dict(
                type='str',
                required=True
            ),
            hcx_enterprise_site_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.private_cloud_name = None
        self.hcx_enterprise_site_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-03-20'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMHcxEnterpriseSiteInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Azure VMware Solution API,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-03-20')

        if (self.resource_group_name is not None and
            self.private_cloud_name is not None and
            self.hcx_enterprise_site_name is not None):
            self.results['hcx_enterprise_sites'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.private_cloud_name is not None):
            self.results['hcx_enterprise_sites'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.hcx_enterprise_sites.get(resource_group_name=self.resource_group_name,
                                                                 private_cloud_name=self.private_cloud_name,
                                                                 hcx_enterprise_site_name=self.hcx_enterprise_site_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.hcx_enterprise_sites.list(resource_group_name=self.resource_group_name,
                                                                  private_cloud_name=self.private_cloud_name)
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
    AzureRMHcxEnterpriseSiteInfo()


if __name__ == '__main__':
    main()
