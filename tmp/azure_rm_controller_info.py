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
module: azure_rm_controller_info
version_added: '2.9'
short_description: Get Controller info.
description:
  - Get info of Controller.
options:
  resource_group_name:
    description:
      - >-
        The name of the Azure Resource group of which a given DelegatedNetwork
        resource is part. This name must be at least 1 character in length, and
        no more than 90.
    required: true
    type: str
  resource_name:
    description:
      - >-
        The name of the resource. It must be a minimum of 3 characters, and a
        maximum of 63.
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get details of a controller
      azure_rm_controller_info: 
        resource_group_name: TestRG
        resource_name: dnctestcontroller
        

'''

RETURN = '''
controller:
  description: >-
    A list of dict results where the key is the name of the Controller and the
    values are the facts for that Controller.
  returned: always
  type: complex
  contains:
    id:
      description:
        - An identifier that represents the DNC controller resource.
      returned: always
      type: str
      sample: null
    name:
      description:
        - The name of the DNC controller resource.
      returned: always
      type: str
      sample: null
    type:
      description:
        - >-
          The type of the DNC controller 
          resource.(Microsoft.DelegatedNetwork/controller)
      returned: always
      type: str
      sample: null
    location:
      description:
        - Location of the DNC controller resource.
      returned: always
      type: str
      sample: null
    state:
      description:
        - The current state of dnc controller resource.
      returned: always
      type: str
      sample: null
    type_properties_type:
      description:
        - Type of dnc controller.
      returned: always
      type: str
      sample: null
    resource_guid:
      description:
        - Gets or sets resource GUID property of the controller resource.
      returned: always
      type: str
      sample: null
    dnc_app_id:
      description:
        - Get controller AAD ID.
      returned: always
      type: str
      sample: null
    dnc_endpoint:
      description:
        - Dnc Endpoint url.
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
    from azure.mgmt.dnc import DNC
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMControllerInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            resource_name=dict(
                type='str',
                required=True
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
        self.query_parameters['api-version'] = '2020-08-08-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMControllerInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(DNC,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-08-08-preview')

        if (self.resource_group_name is not None and
            self.resource_name is not None):
            self.results['controller'] = self.format_item(self.getdetail())
        return self.results

    def getdetail(self):
        response = None

        try:
            response = self.mgmt_client.controller.get_detail(resource_group_name=self.resource_group_name,
                                                              resource_name=self.resource_name)
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
    AzureRMControllerInfo()


if __name__ == '__main__':
    main()
