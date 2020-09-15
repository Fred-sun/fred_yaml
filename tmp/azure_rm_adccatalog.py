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
module: azure_rm_adccatalog
version_added: '2.9'
short_description: Manage Azure ADCCatalog instance.
description:
  - 'Create, update and delete instance of Azure ADCCatalog.'
options:
  resource_group_name:
    description:
      - >-
        The name of the resource group within the user's subscription. The name
        is case insensitive.
    required: true
    type: str
  catalogname:
    description:
      - >-
        The name of the data catalog in the specified subscription and resource
        group.
    required: true
    type: str
  location:
    description:
      - Resource location
    type: str
  etag:
    description:
      - Resource etag
    type: str
  sku:
    description:
      - Azure data catalog SKU.
    type: str
    choices:
      - Free
      - Standard
  units:
    description:
      - Azure data catalog units.
    type: integer
  admins:
    description:
      - Azure data catalog admin list.
    type: list
    suboptions:
      upn:
        description:
          - UPN of the user.
        type: str
      object_id:
        description:
          - Object Id for the user
        type: str
  users:
    description:
      - Azure data catalog user list.
    type: list
    suboptions:
      upn:
        description:
          - UPN of the user.
        type: str
      object_id:
        description:
          - Object Id for the user
        type: str
  successfully_provisioned:
    description:
      - Azure data catalog provision status.
    type: bool
  enable_automatic_unit_adjustment:
    description:
      - Automatic unit adjustment enabled or not.
    type: bool
  state:
    description:
      - Assert the state of the ADCCatalog.
      - >-
        Use C(present) to create or update an ADCCatalog and C(absent) to delete
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
    - name: Create Azure Data Catalog Service
      azure_rm_adccatalog: 
        resource_group_name: exampleResourceGroup
        location: North US
        properties:
          admins:
            - object_id: 99999999-9999-9999-999999999999
              upn: myupn@microsoft.com
          enable_automatic_unit_adjustment: false
          sku: Standard
          units: 1
          users:
            - object_id: 99999999-9999-9999-999999999999
              upn: myupn@microsoft.com
        tags:
          mykey: myvalue
          mykey2: myvalue2
        

    - name: Delete Azure Data Catalog Service
      azure_rm_adccatalog: 
        resource_group_name: exampleResourceGroup
        

    - name: Update Azure Data Catalog Service
      azure_rm_adccatalog: 
        resource_group_name: exampleResourceGroup
        location: North US
        properties:
          admins:
            - object_id: 99999999-9999-9999-999999999999
              upn: myupn@microsoft.com
          enable_automatic_unit_adjustment: false
          sku: Standard
          units: 1
          users:
            - object_id: 99999999-9999-9999-999999999999
              upn: myupn@microsoft.com
        tags:
          mykey: myvalue
          mykey2: myvalue2
        

'''

RETURN = '''
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
sku:
  description:
    - Azure data catalog SKU.
  returned: always
  type: str
  sample: null
units:
  description:
    - Azure data catalog units.
  returned: always
  type: integer
  sample: null
admins:
  description:
    - Azure data catalog admin list.
  returned: always
  type: list
  sample: null
  contains:
    upn:
      description:
        - UPN of the user.
      returned: always
      type: str
      sample: null
    object_id:
      description:
        - Object Id for the user
      returned: always
      type: str
      sample: null
users:
  description:
    - Azure data catalog user list.
  returned: always
  type: list
  sample: null
  contains:
    upn:
      description:
        - UPN of the user.
      returned: always
      type: str
      sample: null
    object_id:
      description:
        - Object Id for the user
      returned: always
      type: str
      sample: null
successfully_provisioned:
  description:
    - Azure data catalog provision status.
  returned: always
  type: bool
  sample: null
enable_automatic_unit_adjustment:
  description:
    - Automatic unit adjustment enabled or not.
  returned: always
  type: bool
  sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.data import DataCatalogRestClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMADCCatalog(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            catalogname=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            etag=dict(
                type='str',
                disposition='/etag'
            ),
            sku=dict(
                type='str',
                disposition='/sku',
                choices=['Free',
                         'Standard']
            ),
            units=dict(
                type='integer',
                disposition='/units'
            ),
            admins=dict(
                type='list',
                disposition='/admins',
                elements='dict',
                options=dict(
                    upn=dict(
                        type='str',
                        disposition='upn'
                    ),
                    object_id=dict(
                        type='str',
                        disposition='object_id'
                    )
                )
            ),
            users=dict(
                type='list',
                disposition='/users',
                elements='dict',
                options=dict(
                    upn=dict(
                        type='str',
                        disposition='upn'
                    ),
                    object_id=dict(
                        type='str',
                        disposition='object_id'
                    )
                )
            ),
            successfully_provisioned=dict(
                type='bool',
                disposition='/successfully_provisioned'
            ),
            enable_automatic_unit_adjustment=dict(
                type='bool',
                disposition='/enable_automatic_unit_adjustment'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.catalogname = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMADCCatalog, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(DataCatalogRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2016-03-30')

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
            response = self.mgmt_client.adccatalogs.create_or_update(resource_group_name=self.resource_group_name,
                                                                     catalogname=self.catalogname,
                                                                     properties=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ADCCatalog instance.')
            self.fail('Error creating the ADCCatalog instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.adccatalogs.delete(resource_group_name=self.resource_group_name,
                                                           catalogname=self.catalogname)
        except CloudError as e:
            self.log('Error attempting to delete the ADCCatalog instance.')
            self.fail('Error deleting the ADCCatalog instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.adccatalogs.get(resource_group_name=self.resource_group_name,
                                                        catalogname=self.catalogname)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMADCCatalog()


if __name__ == '__main__':
    main()
