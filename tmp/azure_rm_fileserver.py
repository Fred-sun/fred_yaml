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
module: azure_rm_fileserver
version_added: '2.9'
short_description: Manage Azure FileServer instance.
description:
  - 'Create, update and delete instance of Azure FileServer.'
options:
  device_name:
    description:
      - The device name.
    required: true
    type: str
  file_server_name:
    description:
      - The file server name.
    required: true
    type: str
  resource_group_name:
    description:
      - The resource group name
    required: true
    type: str
  manager_name:
    description:
      - The manager name
    required: true
    type: str
  domain_name:
    description:
      - Domain of the file server
    type: str
  storage_domain_id:
    description:
      - The storage domain id.
    type: str
  backup_schedule_group_id:
    description:
      - The backup policy id.
    type: str
  description:
    description:
      - The description of the file server
    type: str
  state:
    description:
      - Assert the state of the FileServer.
      - >-
        Use C(present) to create or update an FileServer and C(absent) to delete
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
    - name: FileServersCreateOrUpdate
      azure_rm_fileserver: 
        device_name: HSDK-4XY4FI2IVG
        file_server_name: HSDK-4XY4FI2IVG
        manager_name: hAzureSDKOperations
        resource_group_name: ResourceGroupForSDKTest
        

    - name: FileServersDelete
      azure_rm_fileserver: 
        device_name: HSDK-DMNJB2PET0
        file_server_name: HSDK-DMNJB2PET0
        manager_name: hAzureSDKOperations
        resource_group_name: ResourceGroupForSDKTest
        

'''

RETURN = '''
id:
  description:
    - The identifier.
  returned: always
  type: str
  sample: null
name:
  description:
    - The name.
  returned: always
  type: str
  sample: null
type:
  description:
    - The type.
  returned: always
  type: str
  sample: null
domain_name:
  description:
    - Domain of the file server
  returned: always
  type: str
  sample: null
storage_domain_id:
  description:
    - The storage domain id.
  returned: always
  type: str
  sample: null
backup_schedule_group_id:
  description:
    - The backup policy id.
  returned: always
  type: str
  sample: null
description:
  description:
    - The description of the file server
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
    from azure.mgmt.stor import StorSimpleManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMFileServer(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            device_name=dict(
                type='str',
                required=True
            ),
            file_server_name=dict(
                type='str',
                required=True
            ),
            resource_group_name=dict(
                type='str',
                required=True
            ),
            manager_name=dict(
                type='str',
                required=True
            ),
            domain_name=dict(
                type='str',
                disposition='/domain_name'
            ),
            storage_domain_id=dict(
                type='str',
                disposition='/storage_domain_id'
            ),
            backup_schedule_group_id=dict(
                type='str',
                disposition='/backup_schedule_group_id'
            ),
            description=dict(
                type='str',
                disposition='/description'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.device_name = None
        self.file_server_name = None
        self.resource_group_name = None
        self.manager_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMFileServer, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(StorSimpleManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2016-10-01')

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
            response = self.mgmt_client.file_servers.create_or_update(device_name=self.device_name,
                                                                      file_server_name=self.file_server_name,
                                                                      resource_group_name=self.resource_group_name,
                                                                      manager_name=self.manager_name,
                                                                      file_server=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the FileServer instance.')
            self.fail('Error creating the FileServer instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.file_servers.delete(device_name=self.device_name,
                                                            file_server_name=self.file_server_name,
                                                            resource_group_name=self.resource_group_name,
                                                            manager_name=self.manager_name)
        except CloudError as e:
            self.log('Error attempting to delete the FileServer instance.')
            self.fail('Error deleting the FileServer instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.file_servers.get(device_name=self.device_name,
                                                         file_server_name=self.file_server_name,
                                                         resource_group_name=self.resource_group_name,
                                                         manager_name=self.manager_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMFileServer()


if __name__ == '__main__':
    main()
