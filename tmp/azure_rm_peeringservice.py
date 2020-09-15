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
module: azure_rm_peeringservice
version_added: '2.9'
short_description: Manage Azure PeeringService instance.
description:
  - 'Create, update and delete instance of Azure PeeringService.'
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  peering_service_name:
    description:
      - The name of the peering.
      - The name of the peering service.
    required: true
    type: str
  location:
    description:
      - The location of the resource.
    type: str
  peering_service_location:
    description:
      - The PeeringServiceLocation of the Customer.
    type: str
  peering_service_provider:
    description:
      - The MAPS Provider Name.
    type: str
  name:
    description:
      - The name of the peering service SKU.
    type: str
  state:
    description:
      - Assert the state of the PeeringService.
      - >-
        Use C(present) to create or update an PeeringService and C(absent) to
        delete it.
    default: present
    choices:
      - absent
      - present
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Create a  peering service
      azure_rm_peeringservice: 
        peering_service_name: peeringServiceName
        resource_group_name: rgName
        

    - name: Delete a peering service
      azure_rm_peeringservice: 
        peering_service_name: peeringServiceName
        resource_group_name: rgName
        

    - name: Update peering service tags
      azure_rm_peeringservice: 
        peering_service_name: peeringServiceName
        resource_group_name: rgName
        tags:
          tag0: value0
          tag1: value1
        

'''

RETURN = '''
name:
  description:
    - The name of the resource.
  returned: always
  type: str
  sample: null
id:
  description:
    - The ID of the resource.
  returned: always
  type: str
  sample: null
type:
  description:
    - The type of the resource.
  returned: always
  type: str
  sample: null
location:
  description:
    - The location of the resource.
  returned: always
  type: str
  sample: null
tags:
  description:
    - The resource tags.
  returned: always
  type: dictionary
  sample: null
peering_service_location:
  description:
    - The PeeringServiceLocation of the Customer.
  returned: always
  type: str
  sample: null
peering_service_provider:
  description:
    - The MAPS Provider Name.
  returned: always
  type: str
  sample: null
provisioning_state:
  description:
    - The provisioning state of the resource.
  returned: always
  type: str
  sample: null
name_sku_name:
  description:
    - The name of the peering service SKU.
  returned: always
  type: str
  sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.peering import PeeringManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMPeeringService(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            peering_service_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            peering_service_location=dict(
                type='str',
                disposition='/peering_service_location'
            ),
            peering_service_provider=dict(
                type='str',
                disposition='/peering_service_provider'
            ),
            name=dict(
                type='str',
                disposition='/name'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.peering_service_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMPeeringService, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                    supports_check_mode=True,
                                                    supports_tags=True)

    def exec_module(self, **kwargs):
        for key in list(self.module_arg_spec.keys()):
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                self.body[key] = kwargs[key]

        self.inflate_parameters(self.module_arg_spec, self.body, 0)

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(PeeringManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-04-01')

        old_response = self.get_resource()

        if not old_response:
            if self.state == 'present':
                self.to_do = Actions.Create
        else:
            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                self.results['modifiers'] = modifiers
                self.results['compare'] = []
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            response = self.create_update_resource()
        elif self.to_do == Actions.Delete:
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            self.delete_resource()
        else:
            self.results['changed'] = False
            response = old_response

        return self.results

    def create_update_resource(self):
        try:
            response = self.mgmt_client.peering_services.create_or_update(resource_group_name=self.resource_group_name,
                                                                          peering_service_name=self.peering_service_name,
                                                                          peering_service=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the PeeringService instance.')
            self.fail('Error creating the PeeringService instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.peering_services.delete(resource_group_name=self.resource_group_name,
                                                                peering_service_name=self.peering_service_name)
        except CloudError as e:
            self.log('Error attempting to delete the PeeringService instance.')
            self.fail('Error deleting the PeeringService instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.peering_services.get(resource_group_name=self.resource_group_name,
                                                             peering_service_name=self.peering_service_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMPeeringService()


if __name__ == '__main__':
    main()
