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
module: azure_rm_service
version_added: '2.9'
short_description: Manage Azure Service instance.
description:
  - 'Create, update and delete instance of Azure Service.'
options:
  resource_group_name:
    description:
      - >-
        The name of the resource group that contains the Windows IoT Device
        Service.
    required: true
    type: str
  device_name:
    description:
      - The name of the Windows IoT Device Service.
    required: true
    type: str
  if_match:
    description:
      - >-
        ETag of the Windows IoT Device Service. Do not specify for creating a
        new Windows IoT Device Service. Required to update an existing Windows
        IoT Device Service.
      - >-
        ETag of the Windows IoT Device Service. Do not specify for creating a
        brand new Windows IoT Device Service. Required to update an existing
        Windows IoT Device Service.
    type: str
  notes:
    description:
      - Windows IoT Device Service notes.
    type: str
  quantity:
    description:
      - 'Windows IoT Device Service device allocation,'
    type: integer
  billing_domain_name:
    description:
      - Windows IoT Device Service ODM AAD domain
    type: str
  admin_domain_name:
    description:
      - Windows IoT Device Service OEM AAD domain
    type: str
  state:
    description:
      - Assert the state of the Service.
      - >-
        Use C(present) to create or update an Service and C(absent) to delete
        it.
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
    - name: Service_Create
      azure_rm_service: 
        device_name: service4445
        resource_group_name: res9101
        

    - name: Service_Update
      azure_rm_service: 
        device_name: service8596
        resource_group_name: res9407
        

    - name: Service_Delete
      azure_rm_service: 
        device_name: service2434
        resource_group_name: res4228
        

'''

RETURN = '''
tags:
  description:
    - Resource tags.
  returned: always
  type: dictionary
  sample: null
location:
  description:
    - The Azure Region where the resource lives
  returned: always
  type: str
  sample: null
etag:
  description:
    - >-
      The Etag field is *not* required. If it is provided in the response body,
      it must also be provided as a header per the normal ETag convention.
  returned: always
  type: str
  sample: null
notes:
  description:
    - Windows IoT Device Service notes.
  returned: always
  type: str
  sample: null
start_date:
  description:
    - 'Windows IoT Device Service start date,'
  returned: always
  type: str
  sample: null
quantity:
  description:
    - 'Windows IoT Device Service device allocation,'
  returned: always
  type: integer
  sample: null
billing_domain_name:
  description:
    - Windows IoT Device Service ODM AAD domain
  returned: always
  type: str
  sample: null
admin_domain_name:
  description:
    - Windows IoT Device Service OEM AAD domain
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
    from azure.mgmt.device import DeviceServices
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMService(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            device_name=dict(
                type='str',
                required=True
            ),
            if_match=dict(
                type='str'
            ),
            notes=dict(
                type='str',
                disposition='/notes'
            ),
            quantity=dict(
                type='integer',
                disposition='/quantity'
            ),
            billing_domain_name=dict(
                type='str',
                disposition='/billing_domain_name'
            ),
            admin_domain_name=dict(
                type='str',
                disposition='/admin_domain_name'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.device_name = None
        self.if_match = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMService, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(DeviceServices,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-06-01')

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
            response = self.mgmt_client.services.create_or_update(resource_group_name=self.resource_group_name,
                                                                  device_name=self.device_name,
                                                                  if_match=self.if_match,
                                                                  device_service=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Service instance.')
            self.fail('Error creating the Service instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.services.delete(resource_group_name=self.resource_group_name,
                                                        device_name=self.device_name)
        except CloudError as e:
            self.log('Error attempting to delete the Service instance.')
            self.fail('Error deleting the Service instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.services.get(resource_group_name=self.resource_group_name,
                                                     device_name=self.device_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMService()


if __name__ == '__main__':
    main()
