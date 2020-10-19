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
module: azure_rm_datamanager
version_added: '2.9'
short_description: Manage Azure DataManager instance.
description:
  - 'Create, update and delete instance of Azure DataManager.'
options:
  resource_group_name:
    description:
      - The Resource Group Name
    required: true
    type: str
  data_manager_name:
    description:
      - >-
        The name of the DataManager Resource within the specified resource
        group. DataManager names must be between 3 and 24 characters in length
        and use any alphanumeric and underscore only
    required: true
    type: str
  location:
    description:
      - "The location of the resource. This will be one of the supported and registered Azure Geo Regions (e.g. West US, East\r"
      - "US, Southeast Asia, etc.). The geo region of a resource cannot be changed once it is created, but if an identical geo\r"
      - region is specified on update the request will succeed.
    type: str
  sku:
    description:
      - The sku type.
    type: dict
    suboptions:
      name:
        description:
          - >-
            The sku name. Required for data manager creation, optional for
            update.
        type: str
      tier:
        description:
          - The sku tier. This is based on the SKU name.
        type: str
  etag:
    description:
      - Etag of the Resource.
    type: str
  if_match:
    description:
      - >-
        Defines the If-Match condition. The patch will be performed only if the
        ETag of the data manager resource on the server matches this value.
    type: str
  state:
    description:
      - Assert the state of the DataManager.
      - >-
        Use C(present) to create or update an DataManager and C(absent) to
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
    - name: DataManagers_CreatePUT41
      azure_rm_datamanager: 
        data_manager_name: TestAzureSDKOperations
        resource_group_name: ResourceGroupForSDKTest
        

    - name: DataManagers_DeleteDELETE41
      azure_rm_datamanager: 
        data_manager_name: TestAzureSDKOperations
        resource_group_name: ResourceGroupForSDKTest
        

    - name: DataManagers_UpdatePATCH43
      azure_rm_datamanager: 
        data_manager_name: TestAzureSDKOperations
        resource_group_name: ResourceGroupForSDKTest
        

'''

RETURN = '''
id:
  description:
    - The Resource Id.
  returned: always
  type: str
  sample: null
name:
  description:
    - The Resource Name.
  returned: always
  type: str
  sample: null
type:
  description:
    - The Resource type.
  returned: always
  type: str
  sample: null
location:
  description:
    - "The location of the resource. This will be one of the supported and registered Azure Geo Regions (e.g. West US, East\r\nUS, Southeast Asia, etc.). The geo region of a resource cannot be changed once it is created, but if an identical geo\r\nregion is specified on update the request will succeed."
  returned: always
  type: str
  sample: null
tags:
  description:
    - "The list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource\r\n(across resource groups)."
  returned: always
  type: dictionary
  sample: null
sku:
  description:
    - The sku type.
  returned: always
  type: dict
  sample: null
  contains:
    name:
      description:
        - 'The sku name. Required for data manager creation, optional for update.'
      returned: always
      type: str
      sample: null
    tier:
      description:
        - The sku tier. This is based on the SKU name.
      returned: always
      type: str
      sample: null
etag:
  description:
    - Etag of the Resource.
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
    from azure.mgmt.hybrid import HybridDataManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMDataManager(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            data_manager_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            sku=dict(
                type='dict',
                disposition='/sku',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name'
                    ),
                    tier=dict(
                        type='str',
                        disposition='tier'
                    )
                )
            ),
            etag=dict(
                type='str',
                disposition='/etag'
            ),
            if_match=dict(
                type='str'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.data_manager_name = None
        self.if_match = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMDataManager, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(HybridDataManagementClient,
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
            if self.to_do == Actions.Create:
                response = self.mgmt_client.data_managers.create(resource_group_name=self.resource_group_name,
                                                                 data_manager_name=self.data_manager_name,
                                                                 data_manager=self.body)
            else:
                response = self.mgmt_client.data_managers.update(resource_group_name=self.resource_group_name,
                                                                 data_manager_name=self.data_manager_name,
                                                                 if_match=self.if_match,
                                                                 data_manager_update_parameter=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the DataManager instance.')
            self.fail('Error creating the DataManager instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.data_managers.delete(resource_group_name=self.resource_group_name,
                                                             data_manager_name=self.data_manager_name)
        except CloudError as e:
            self.log('Error attempting to delete the DataManager instance.')
            self.fail('Error deleting the DataManager instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.data_managers.get(resource_group_name=self.resource_group_name,
                                                          data_manager_name=self.data_manager_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMDataManager()


if __name__ == '__main__':
    main()
