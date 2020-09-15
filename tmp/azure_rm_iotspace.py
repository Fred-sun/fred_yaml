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
module: azure_rm_iotspace
version_added: '2.9'
short_description: Manage Azure IoTSpace instance.
description:
  - 'Create, update and delete instance of Azure IoTSpace.'
options:
  resource_group_name:
    description:
      - The name of the resource group that contains the IoTSpaces instance.
    required: true
    type: str
  resource_name:
    description:
      - The name of the IoTSpaces instance.
    required: true
    type: str
  location:
    description:
      - The resource location.
    type: str
  name:
    description:
      - The name of the SKU.
    type: str
    choices:
      - F1
      - S1
      - S2
      - S3
  storage_container:
    description:
      - The properties of the designated storage container.
    type: dict
    suboptions:
      connection_string:
        description:
          - The connection string of the storage account.
        type: str
      subscription_id:
        description:
          - The subscription identifier of the storage account.
        type: str
      resource_group:
        description:
          - The name of the resource group of the storage account.
        type: str
      container_name:
        description:
          - The name of storage container in the storage account.
        type: str
  state:
    description:
      - Assert the state of the IoTSpace.
      - >-
        Use C(present) to create or update an IoTSpace and C(absent) to delete
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
    - name: Put an IoT spaces service
      azure_rm_iotspace: 
        resource_group_name: resRg
        resource_name: myIoTSpacesService
        

    - name: Patch an IoT spaces service
      azure_rm_iotspace: 
        resource_group_name: resRg
        resource_name: myIoTSpacesService
        

    - name: Delete an IoT spaces service
      azure_rm_iotspace: 
        resource_group_name: resRg
        resource_name: myIoTSpacesService
        

'''

RETURN = '''
id:
  description:
    - The resource identifier.
  returned: always
  type: str
  sample: null
name:
  description:
    - The resource name.
  returned: always
  type: str
  sample: null
type:
  description:
    - The resource type.
  returned: always
  type: str
  sample: null
location:
  description:
    - The resource location.
  returned: always
  type: str
  sample: null
tags:
  description:
    - The resource tags.
  returned: always
  type: dictionary
  sample: null
name_sku_name:
  description:
    - The name of the SKU.
  returned: always
  type: str
  sample: null
provisioning_state:
  description:
    - The provisioning state.
  returned: always
  type: str
  sample: null
management_api_url:
  description:
    - The management Api endpoint.
  returned: always
  type: str
  sample: null
web_portal_url:
  description:
    - The management UI endpoint.
  returned: always
  type: str
  sample: null
storage_container:
  description:
    - The properties of the designated storage container.
  returned: always
  type: dict
  sample: null
  contains:
    connection_string:
      description:
        - The connection string of the storage account.
      returned: always
      type: str
      sample: null
    subscription_id:
      description:
        - The subscription identifier of the storage account.
      returned: always
      type: str
      sample: null
    resource_group:
      description:
        - The name of the resource group of the storage account.
      returned: always
      type: str
      sample: null
    container_name:
      description:
        - The name of storage container in the storage account.
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
    from azure.mgmt.io import IoTSpacesClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMIoTSpace(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            resource_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            name=dict(
                type='str',
                disposition='/name',
                choices=['F1',
                         'S1',
                         'S2',
                         'S3']
            ),
            storage_container=dict(
                type='dict',
                disposition='/storage_container',
                options=dict(
                    connection_string=dict(
                        type='str',
                        disposition='connection_string'
                    ),
                    subscription_id=dict(
                        type='str',
                        disposition='subscription_id'
                    ),
                    resource_group=dict(
                        type='str',
                        disposition='resource_group'
                    ),
                    container_name=dict(
                        type='str',
                        disposition='container_name'
                    )
                )
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.resource_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMIoTSpace, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(IoTSpacesClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-10-01-preview')

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
            response = self.mgmt_client.io_tspaces.create_or_update(resource_group_name=self.resource_group_name,
                                                                    resource_name=self.resource_name,
                                                                    iot_space_description=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the IoTSpace instance.')
            self.fail('Error creating the IoTSpace instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.io_tspaces.delete(resource_group_name=self.resource_group_name,
                                                          resource_name=self.resource_name)
        except CloudError as e:
            self.log('Error attempting to delete the IoTSpace instance.')
            self.fail('Error deleting the IoTSpace instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.io_tspaces.get(resource_group_name=self.resource_group_name,
                                                       resource_name=self.resource_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMIoTSpace()


if __name__ == '__main__':
    main()
