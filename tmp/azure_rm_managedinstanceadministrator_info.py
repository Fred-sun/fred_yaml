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
module: azure_rm_managedinstanceadministrator_info
version_added: '2.9'
short_description: Get ManagedInstanceAdministrator info.
description:
  - Get info of ManagedInstanceAdministrator.
options:
  resource_group_name:
    description:
      - >-
        The name of the resource group that contains the resource. You can
        obtain this value from the Azure Resource Manager API or the portal.
    required: true
    type: str
  managed_instance_name:
    description:
      - The name of the managed instance.
    required: true
    type: str
  administratorname:
    description:
      - The administrator name.
    type: constant
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List administrators of managed instance
      azure_rm_managedinstanceadministrator_info: 
        managed_instance_name: managedInstance
        resource_group_name: Default-SQL-SouthEastAsia
        

    - name: Get administrator of managed instance
      azure_rm_managedinstanceadministrator_info: 
        managed_instance_name: managedInstance
        resource_group_name: Default-SQL-SouthEastAsia
        

'''

RETURN = '''
managed_instance_administrators:
  description: >-
    A list of dict results where the key is the name of the
    ManagedInstanceAdministrator and the values are the facts for that
    ManagedInstanceAdministrator.
  returned: always
  type: complex
  contains:
    value:
      description:
        - Array of results.
      returned: always
      type: list
      sample: null
      contains:
        administrator_type:
          description:
            - Type of the managed instance administrator.
          returned: always
          type: str
          sample: null
        login:
          description:
            - Login name of the managed instance administrator.
          returned: always
          type: str
          sample: null
        sid:
          description:
            - SID (object ID) of the managed instance administrator.
          returned: always
          type: uuid
          sample: null
        tenant_id:
          description:
            - Tenant ID of the managed instance administrator.
          returned: always
          type: uuid
          sample: null
    next_link:
      description:
        - Link to retrieve next page of results.
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
    administrator_type:
      description:
        - Type of the managed instance administrator.
      returned: always
      type: str
      sample: null
    login:
      description:
        - Login name of the managed instance administrator.
      returned: always
      type: str
      sample: null
    sid:
      description:
        - SID (object ID) of the managed instance administrator.
      returned: always
      type: uuid
      sample: null
    tenant_id:
      description:
        - Tenant ID of the managed instance administrator.
      returned: always
      type: uuid
      sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.sql import SqlManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMManagedInstanceAdministratorInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            managed_instance_name=dict(
                type='str',
                required=True
            ),
            administratorname=dict(
                type='constant'
            )
        )

        self.resource_group_name = None
        self.managed_instance_name = None
        self.administratorname = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-03-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMManagedInstanceAdministratorInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-03-01-preview')

        if (self.resource_group_name is not None and
            self.managed_instance_name is not None and
            self.administratorname is not None):
            self.results['managed_instance_administrators'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.managed_instance_name is not None):
            self.results['managed_instance_administrators'] = self.format_item(self.listbyinstance())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.managed_instance_administrators.get(resource_group_name=self.resource_group_name,
                                                                            managed_instance_name=self.managed_instance_name,
                                                                            administratorname=self.administratorname)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyinstance(self):
        response = None

        try:
            response = self.mgmt_client.managed_instance_administrators.list_by_instance(resource_group_name=self.resource_group_name,
                                                                                         managed_instance_name=self.managed_instance_name)
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
    AzureRMManagedInstanceAdministratorInfo()


if __name__ == '__main__':
    main()
